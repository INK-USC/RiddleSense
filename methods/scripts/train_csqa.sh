DATA_DIR=models/data_dir/csqa_to_rs
MODEL_DIR=~/riddle_models/csqa_bert_base
CUDA_VISIBLE_DEVICES=2,3  python models/run_mcqa.py \
    --task_name riddleqa \
    --model_name_or_path bert-base-uncased \
    --do_train \
    --do_eval \
    --data_dir $DATA_DIR \
    --train_file ${DATA_DIR}/csqa_train.jsonl \
    --val_file ${DATA_DIR}/rs_dev.jsonl \
    --evaluate_during_training \
    --evaluation_strategy steps \
    --load_best_model_at_end \
    --metric_for_best_model eval_acc \
    --greater_is_better True \
    --eval_steps 200 \
    --num_choices 5 \
    --learning_rate 3e-5 \
    --num_train_epochs 10 \
    --max_seq_length 100 \
    --output_dir ${MODEL_DIR} \
    --per_device_eval_batch_size=8 \
    --per_device_train_batch_size=8 \
    --gradient_accumulation_steps 2 \
    --fp16 --overwrite_output \
    --overwrite_cache \
    --do_predict \
    --test_file ${DATA_DIR}/rs_test.jsonl \
    --prediction_output ${DATA_DIR}/results/bert_base_c2r_result.npy 


DATA_DIR=models/data_dir/csqa_to_rs
MODEL_DIR=~/riddle_models/csqa_bert_large
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7  python models/run_mcqa.py \
    --task_name riddleqa \
    --model_name_or_path bert-large-uncased \
    --do_train \
    --do_eval \
    --data_dir $DATA_DIR \
    --train_file ${DATA_DIR}/csqa_train.jsonl \
    --val_file ${DATA_DIR}/rs_dev.jsonl \
    --evaluate_during_training \
    --evaluation_strategy steps \
    --load_best_model_at_end \
    --metric_for_best_model eval_acc \
    --greater_is_better True \
    --eval_steps 200 \
    --num_choices 5 \
    --learning_rate 3e-5 \
    --num_train_epochs 10 \
    --max_seq_length 100 \
    --output_dir ${MODEL_DIR} \
    --per_device_eval_batch_size=8 \
    --per_device_train_batch_size=8 \
    --gradient_accumulation_steps 2 \
    --fp16 --overwrite_output \
    --overwrite_cache \
    --do_predict \
    --test_file ${DATA_DIR}/rs_test.jsonl \
    --prediction_output ${DATA_DIR}/results/bert_large_c2r_result.npy 


DATA_DIR=models/data_dir/csqa_to_rs/
MODEL_DIR=~/riddle_models/csqa_roberta_large
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7  python models/run_mcqa.py \
    --task_name riddleqa \
    --model_name_or_path roberta-large \
    --do_train \
    --do_eval \
    --data_dir $DATA_DIR \
    --train_file ${DATA_DIR}/csqa_train.jsonl \
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
    --prediction_output ${DATA_DIR}/results/roberta_large_c2r_result.npy 

DATA_DIR=models/data_dir/csqa_to_rs/
MODEL_DIR=~/riddle_models/csqa_albert_xxlarge
rm -rf $MODEL_DIR
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python models/run_mcqa.py \
    --task_name riddleqa \
    --model_name_or_path albert-xxlarge-v2 \
    --do_train \
    --do_eval \
    --data_dir $DATA_DIR \
    --train_file ${DATA_DIR}/csqa_train.jsonl \
    --val_file ${DATA_DIR}/rs_dev.jsonl \
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
    --do_predict \
    --test_file ${DATA_DIR}/rs_test.jsonl \
    --prediction_output ${DATA_DIR}/results/albert_xxl_c2r_result.npy 