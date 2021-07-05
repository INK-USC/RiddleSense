#!/bin/bash
#SBATCH --gres=gpu:4
source /home/danny911kr/miniconda3/etc/profile.d/conda.sh
conda activate t5-stable

python models/t5/finetune.py \
--data_dir models/data_dir/riddle_sense \
--output_dir models/t5/checkpoints/unifiedqa-3b \
--model_name_or_path allenai/unifiedqa-t5-3b \
--tokenizer_name_or_path allenai/unifiedqa-t5-3b \
--learning_rate 3e-4 \
--max_seq_length 128 \
--train_batch_size 16 \
--gradient_accumulation_steps 4 \
--model_parallel True
