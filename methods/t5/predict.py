import torch
import csv
import argparse
from trainer import *
from tqdm import tqdm
import random
import numpy as np
import os
import re
import glob
from transformers import (
    AdamW,
    T5ForConditionalGeneration,
    T5Tokenizer,
    get_linear_schedule_with_warmup,
    AutoTokenizer
)
from dataset import RiddleSenseProcessor

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def extractValLoss(checkpoint_path):
    """Eg checkpoint path format: path_to_dir/checkpoint_epoch=4-val_loss=0.450662.ckpt"""
    val_loss = float(re.search('val_loss=(.+?).ckpt', checkpoint_path).group(1))
    return val_loss

def extractStepOREpochNum(checkpoint_path):
    """Eg checkpoint path format: path_to_dir/checkpoint_epoch=4.ckpt (or)
        path_to_dir/checkpoint_epoch=4-step=50.ckpt (or)
    """
    if "step" in checkpoint_path:
        num = int(re.search('step=(.+?).ckpt', checkpoint_path).group(1))
    else:
        num = int(re.search('epoch=(.+?).ckpt', checkpoint_path).group(1))
    return num

def getBestModelCheckpointPath(checkpoint_dir):
    checkpoint_list = glob.glob(os.path.join(checkpoint_dir, "checkpoint_*.ckpt"))

    try:
        # Get the checkpoint with lowest validation loss
        sorted_list = sorted(checkpoint_list, key=lambda x: extractValLoss(x.split("/")[-1]))
    except:
        # If validation loss is not present, get the checkpoint with highest step number or epoch number.
        sorted_list = sorted(checkpoint_list, key=lambda x: extractStepOREpochNum(x.split("/")[-1]), reverse=True)

    return sorted_list[0]

def run():
    #torch.multiprocessing.freeze_support()
    set_seed(42)

    parser = argparse.ArgumentParser()

    parser.add_argument('--data_dir', type=str, default="../data_dir/riddle_sense",
                        help='Path for Data files')
    parser.add_argument('--output_dir', type=str, default="",
                        help='Path to save the checkpoints')
    parser.add_argument('--checkpoint_dir', type=str, default="",
                        help='Checkpoint directory')
    parser.add_argument('--tokenizer_name_or_path', type=str, default="",
                        help='Tokenizer name or Path')
    parser.add_argument('--max_seq_length', type=int, default=128,
                        help='Maximum Sequence Length')
    parser.add_argument('--eval_batch_size', type=int, default=8,
                        help='Batch size for Evaluation')

    args = parser.parse_known_args()[0]
    print(args)

    # Create a folder if output_dir doesn't exists:
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
        print("Creating output directory")

    if args.checkpoint_dir == "":
        model_name = args.model_name_or_path #"allenai/t5-t5-3b"  # you can specify the model size here
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = T5ForConditionalGeneration.from_pretrained(model_name)
    else:
        best_checkpoint_path = getBestModelCheckpointPath(args.checkpoint_dir)
        print("Using checkpoint = ", str(best_checkpoint_path))
        tokenizer = T5Tokenizer.from_pretrained(args.tokenizer_name_or_path)
        model = T5FineTuner.load_from_checkpoint(best_checkpoint_path).model

    proc = RiddleSenseProcessor()
    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i : i + n]

    dev_csvfile = open(os.path.join(args.output_dir, 'dev.csv'),'w')
    dev_writer = csv.writer(dev_csvfile)
    dev_examples = proc.get_dev_examples(args.data_dir)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(device)
    model.to(device)

    for batch in tqdm(list(chunks(dev_examples, args.eval_batch_size))):
        batch_question = [b.question for b in batch]
        options = [['(%s) %s' % (i, option) for i, option in zip(['A','B','C','D','E'], b.endings)] for b in batch]
        options = [" ".join(opts) for opts in options]

        inputs = []
        for question, option in zip(batch_question, options):
            inputs.append("%s \\n %s" % (question, option))
        dct = tokenizer.batch_encode_plus(inputs, max_length=args.max_seq_length, return_tensors="pt", padding=True, truncation=True)
        outs = model.generate(input_ids=dct['input_ids'].to(device),
                              attention_mask=dct['attention_mask'].to(device))

        dec = [tokenizer.decode(x, skip_special_tokens=True, clean_up_tokenization_spaces=True) for x in outs]
        ids = [b.example_id for b in batch]

        for i, d in zip(ids, dec):
            dev_writer.writerow([i,d])

    test_csvfile = open(os.path.join(args.output_dir, 'test.csv'),'w')
    test_writer = csv.writer(test_csvfile)
    test_examples = proc.get_test_examples(args.data_dir, num_choices=5)

    for batch in tqdm(list(chunks(test_examples, args.eval_batch_size))):
        batch_question = [b.question for b in batch]
        options = [['(%s) %s' % (i, option) for i, option in zip(['A','B','C','D','E'], b.endings)] for b in batch]
        options = [" ".join(opts) for opts in options]

        inputs = []
        for question, option in zip(batch_question, options):
            inputs.append("%s \\n %s" % (question, option))

        dct = tokenizer.batch_encode_plus(inputs, max_length=args.max_seq_length, return_tensors="pt", padding=True, truncation=True)
        outs = model.generate(input_ids=dct['input_ids'].to(device),
                              attention_mask=dct['attention_mask'].to(device))

        dec = [tokenizer.decode(x, skip_special_tokens=True, clean_up_tokenization_spaces=True) for x in outs]
        ids = [b.example_id for b in batch]

        for i, d in zip(ids, dec):
            test_writer.writerow([i,d])


if __name__ == '__main__':
    run()
