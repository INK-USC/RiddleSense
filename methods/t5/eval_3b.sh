#!/bin/bash
#SBATCH --gres=gpu:4
source /home/danny911kr/miniconda3/etc/profile.d/conda.sh
conda activate t5-stable

python models/t5/predict.py \
--data_dir models/data_dir/riddle_sense \
--tokenizer_name_or_path allenai/unifiedqa-t5-3b \
--checkpoint_dir models/t5/checkpoints/unifiedqa-3b \
--output_dir models/t5/outputs/unifiedqa-3b-finetune \
--max_seq_length 128 \
--eval_batch_size 4
