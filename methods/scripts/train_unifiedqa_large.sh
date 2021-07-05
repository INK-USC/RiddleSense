DATA_DIR=data_dir/
MODEL_DIR=~/riddle_models/unifiedqa_large
python models/t5/finetune.py \
    --data_dir ${DATA_DIR} \
    --output_dir ${MODEL_DIR} \
    --model_name_or_path allenai/unifiedqa-t5-large \
    --tokenizer_name_or_path allenai/unifiedqa-t5-large \
    --learning_rate 3e-4 \
    --max_seq_length 100 \
    --train_batch_size 8 \
    --gradient_accumulation_steps 8 \
    --num_train_epochs 30 \
    --fp_16 \
    --gpu_nums "0,1,2,3,4,5,6,7"