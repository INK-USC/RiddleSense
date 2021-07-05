# DATA_DIR=models/data_dir/csqa_to_rs/
# MODEL_DIR=~/riddle_models/csqa_rs_roberta_large
# CUDA_VISIBLE_DEVICES=0,1,2,3 python models/run_mcqa.py \
# --task_name riddleqa \
# --model_name_or_path ${MODEL_DIR} \
# --do_eval \
# --data_dir $DATA_DIR \
# --train_file "" --val_file ${DATA_DIR}/rs_test_v1.1.jsonl \
# --test_file "" --prediction_output "" \
# --num_choices 5 \
# --max_seq_length 100 \
# --output_dir ~/riddle_models/csqa_rs_ \
# --per_gpu_eval_batch_size=6 \
# --fp16 --overwrite_output \
# --overwrite_cache

DATA_DIR=models/data_dir/csqa_to_rs/
MODEL_DIR=~/riddle_models/csqa_rs_albert_large
CUDA_VISIBLE_DEVICES=8,9 python models/run_mcqa.py \
--task_name riddleqa \
--model_name_or_path ${MODEL_DIR}/ \
--do_eval \
--data_dir $DATA_DIR \
--train_file "" --val_file ${DATA_DIR}/rs_test_v1.1.jsonl \
--test_file "" --prediction_output "" \
--num_choices 5 \
--max_seq_length 100 \
--output_dir ~/riddle_models/ \
--per_gpu_eval_batch_size=5 \
--fp16 --overwrite_output \
--overwrite_cache