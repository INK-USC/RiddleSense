#!/bin/bash
#SBATCH --gres=gpu:4
source /home/danny911kr/miniconda3/etc/profile.d/conda.sh
conda activate mics

python models/t5/finetune.py \
--data_dir models/data_dir/riddle_sense \
--output_dir models/t5/checkpoints/unifiedqa-large \
--model_name_or_path allenai/unifiedqa-t5-large \
--tokenizer_name_or_path allenai/unifiedqa-t5-large \
--learning_rate 3e-4 \
--max_seq_length 128 \
--train_batch_size 4 \
--gradient_accumulation_steps 16 \
--gpu_nums "-1"
