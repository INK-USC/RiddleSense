import json
import collections
from collections import defaultdict
from tqdm import tqdm
from absl import app, flags
import pickle
import numpy as np               


def eval_npy(prediction_file):
  """Main fucntion.""" 
  instances = []
  with open("models/data_dir/riddle_sense/test.jsonl") as f:
    for line in f.read().splitlines():
      if line:
        instances.append(json.loads(line))
  with open(prediction_file, "rb") as f:
    predictions = pickle.load(f)
  assert len(predictions) == len(instances)

  num_correct = 0
  output_res = []
  for ind, (inst, pred) in enumerate(zip(instances, predictions)):
    question_id = inst["id"]
    choices = inst["question"]["choices"]
    correct_choice = choices[ord(inst["answerKey"])-ord("A")]
    assert correct_choice["label"] == inst["answerKey"]
    assert len(choices) == len(pred)
    ranked_list = [(c["label"], c["text"], float(p)) for c, p in zip(choices, pred)]
    ranked_list.sort(key=lambda x: x[2], reverse=True)

    if ranked_list[0][1] == correct_choice["text"]:
        num_correct += 1
    output_res.append("%s\t%s"%(question_id, ranked_list[0]))
  with open(prediction_file.replace(".npy", ".res"), "w") as f:
    for line in output_res:
          f.write(line+"\n")
  
  print(num_correct/len(instances))

if __name__ == "__main__":
  # RS
  print("RS")
  eval_npy("models/data_dir/riddle_sense/results/bert_base_result.npy")
  eval_npy("models/data_dir/riddle_sense/results/bert_large_result.npy")
  eval_npy("models/data_dir/riddle_sense/results/roberta_large_result.npy")
  eval_npy("models/data_dir/riddle_sense/results/albert_xxl_result.npy")

  # CSQA
  print("CSQA")
  eval_npy("models/data_dir/csqa_to_rs/results/bert_base_c2r_result.npy")
  eval_npy("models/data_dir/csqa_to_rs/results/bert_large_c2r_result.npy")
  eval_npy("models/data_dir/csqa_to_rs/results/roberta_large_c2r_result.npy")
  eval_npy("models/data_dir/csqa_to_rs/results/albert_xxl_c2r_result.npy")

  # RS+CSQA
  print("RS+CSQA")
  eval_npy("models/data_dir/csqa_to_rs/results/bert_base_rc2r_result.npy")
  eval_npy("models/data_dir/csqa_to_rs/results/bert_large_rc2r_result.npy")
  eval_npy("models/data_dir/csqa_to_rs//results/roberta_large_rc2r_result.npy")
  eval_npy("models/data_dir/csqa_to_rs//results/albert_xxl_rc2r_result.npy")
  

  # RS-percentage-RoBERTa
  print("RS-percentage-RoBERTa")
  for i in range(10, 101, 10):
    eval_npy("models/data_dir/riddle_sense/results/roberta_large_result_%d.npy"%i)
  # RS-percentage-ALBERT
  print("RS")
  for i in range(10, 101, 10):
    eval_npy("models/data_dir/riddle_sense/results/albert_xxl_result_%d.npy"%i)
  