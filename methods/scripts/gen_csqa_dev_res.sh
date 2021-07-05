# CSQA models
MODEL_NAME=~/riddle_models/csqa_bert_large
CUDA_VISIBLE_DEVICES=1,2,3,4,5,6,7 python models/run_mcqa.py \
    --task_name riddleqa \
    --model_name_or_path ${MODEL_NAME} \
    --do_eval \
    --data_dir models/data_dir/csqa_to_rs/ \
    --train_file "" \
    --test_file "" --prediction_output "" \
    --val_file models/data_dir/csqa_to_rs/csqa_dev.jsonl \
    --num_choices 5 \
    --max_seq_length 100 \
    --per_gpu_eval_batch_size=8 \
    --fp16 --output_dir "/tmp" \
    --overwrite_cache 

MODEL_NAME=~/riddle_models/csqa_roberta_large
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python models/run_mcqa.py \
    --task_name riddleqa \
    --model_name_or_path ${MODEL_NAME} \
    --do_eval \
    --data_dir models/data_dir/csqa_to_rs/ \
    --train_file "" \
    --test_file "" --prediction_output "" \
    --val_file models/data_dir/csqa_to_rs/csqa_dev.jsonl \
    --num_choices 5 \
    --max_seq_length 100 \
    --per_gpu_eval_batch_size=8 \
    --fp16 --output_dir "/tmp" \
    --overwrite_cache 

MODEL_NAME=~/riddle_models/csqa_albert_xxlarge
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python models/run_mcqa.py \
    --task_name riddleqa \
    --model_name_or_path ${MODEL_NAME} \
    --do_eval \
    --data_dir models/data_dir/csqa_to_rs/ \
    --train_file "" \
    --test_file "" --prediction_output "" \
    --val_file models/data_dir/csqa_to_rs/csqa_dev.jsonl \
    --num_choices 5 \
    --max_seq_length 100 \
    --per_gpu_eval_batch_size=5 \
    --fp16 --output_dir "/tmp" \
    --overwrite_cache 





# RS+CSQA models
MODEL_NAME=~/riddle_models/rc_bert_large
CUDA_VISIBLE_DEVICES=1,2,3,4,5,6,7 python models/run_mcqa.py \
    --task_name riddleqa \
    --model_name_or_path ${MODEL_NAME} \
    --do_eval \
    --data_dir models/data_dir/csqa_to_rs/ \
    --train_file "" \
    --test_file "" --prediction_output "" \
    --val_file models/data_dir/csqa_to_rs/csqa_dev.jsonl \
    --num_choices 5 \
    --max_seq_length 100 \
    --per_gpu_eval_batch_size=1 \
    --fp16 --output_dir "/tmp" \
    --overwrite_cache 

MODEL_NAME=~/riddle_models/rc_roberta_large
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python models/run_mcqa.py \
    --task_name riddleqa \
    --model_name_or_path ${MODEL_NAME} \
    --do_eval \
    --data_dir models/data_dir/csqa_to_rs/ \
    --train_file "" \
    --test_file "" --prediction_output "" \
    --val_file models/data_dir/csqa_to_rs/csqa_dev.jsonl \
    --num_choices 5 \
    --max_seq_length 100 \
    --per_gpu_eval_batch_size=5 \
    --fp16 --output_dir "/tmp" \
    --overwrite_cache 

MODEL_NAME=~/riddle_models/rc_albert_xxlarge
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python models/run_mcqa.py \
    --task_name riddleqa \
    --model_name_or_path ${MODEL_NAME} \
    --do_eval \
    --data_dir models/data_dir/csqa_to_rs/ \
    --train_file "" \
    --test_file "" --prediction_output "" \
    --val_file models/data_dir/csqa_to_rs/csqa_dev.jsonl \
    --num_choices 5 \
    --max_seq_length 100 \
    --per_gpu_eval_batch_size=5 \
    --fp16 --output_dir "/tmp" \
    --overwrite_cache 

