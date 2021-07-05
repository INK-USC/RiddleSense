#!/bin/bash
for i in 10 20 30 40 50 60 70 80 90 100
do
DATA_DIR=models/data_dir/riddle_sense
MODEL_DIR=/tmp/alberta_percentage_${i}
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python models/run_mcqa.py \
    --task_name riddleqa \
    --model_name_or_path albert-xxlarge-v2 \
    --do_train \
    --do_eval \
    --data_dir $DATA_DIR \
    --train_file ${DATA_DIR}/train.jsonl \
    --val_file ${DATA_DIR}/dev.jsonl \
    --evaluate_during_training \
    --evaluation_strategy steps \
    --load_best_model_at_end \
    --metric_for_best_model eval_acc \
    --greater_is_better True \
    --eval_steps 100 \
    --num_choices 5 \
    --learning_rate 1e-5 \
    --num_train_epochs 5 \
    --max_seq_length 100 \
    --output_dir ${MODEL_DIR} \
    --per_device_eval_batch_size=7 \
    --per_device_train_batch_size=3 \
    --gradient_accumulation_steps 2 \
    --warmup_steps 100 \
    --fp16 --overwrite_output \
    --overwrite_cache \
    --save_total_limit 1 \
    --percentage ${i} \
    --do_predict \
    --test_file ${DATA_DIR}/test.jsonl \
    --prediction_output ${DATA_DIR}/results/albert_xxl_result_${i}.npy 
done
