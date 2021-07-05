DATA_DIR=data_dir/
MODEL_DIR=~/riddle_models/roberta_large
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7  python models/run_mcqa.py \
    --task_name riddlesense \
    --model_name_or_path roberta-large \
    --do_train \
    --do_eval \
    --data_dir $DATA_DIR \
    --train_file ${DATA_DIR}/rs_train.jsonl \
    --val_file ${DATA_DIR}/rs_dev.jsonl \
    --evaluate_during_training \
    --evaluation_strategy steps \
    --load_best_model_at_end \
    --metric_for_best_model eval_acc \
    --greater_is_better True \
    --eval_steps 200 \
    --num_choices 5 \
    --learning_rate 1e-5 \
    --num_train_epochs 10 \
    --max_seq_length 100 \
    --output_dir ${MODEL_DIR} \
    --per_device_eval_batch_size=8 \
    --per_device_train_batch_size=8 \
    --gradient_accumulation_steps 2 \
    --warmup_steps 100 \
    --fp16 --overwrite_output \
    --overwrite_cache \
    --do_predict \
    --test_file ${DATA_DIR}/rs_test.jsonl \
    --prediction_output ${DATA_DIR}/results/roberta_large_result.npy 