
# Installation


```bash
conda create --name riddleqa python=3.7
conda activate riddleqa
# pip install torch==1.4.0 torchvision==0.5.0 -f https://download.pytorch.org/whl/cu100/torch_stable.html
# conda install -c anaconda cudatoolkit=10.1 -n riddleqa
# conda install pytorch==1.6.0 torchvision==0.7.0 cudatoolkit=10.1 -c pytorch -n riddleqa
pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html

# git clone https://github.com/huggingface/transformers

cd transformers
pip install .
pip install tensorboardX
pip install absl-py

```

```bash 
git clone https://github.com/NVIDIA/apex
cd apex
pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
```

# Experiments  (RS-->RS) 

```bash
bash models/scripts/train_bert_base.sh
bash models/scripts/train_bert_large.sh
bash models/scripts/train_roberta_large.sh
bash models/scripts/train_albert_xxlarge.sh
echo "finished!"
```


```bash
cat ~/riddle_models/bert_large/eval_results.txt
cat ~/riddle_models/roberta_large/eval_results.txt
cat ~/riddle_models/albert_xxlarge/eval_results.txt


cat ~/riddle_models/csqa_bert_large/eval_results.txt
cat ~/riddle_models/csqa_roberta_large/eval_results.txt
cat ~/riddle_models/csqa_albert_xxlarge/eval_results.txt
```



<!-- ## BERT-Large -->


<!-- ### Test 
```bash   
DATA_DIR=models/data_dir/riddle_sense/
MODEL_DIR=/tmp/riddle_models/riddle_sense/roberta_large/checkpoint-400/
wget https://s3.amazonaws.com/models.huggingface.co/bert/roberta-large-vocab.json -O ${MODEL_DIR}/vocab.json
wget https://s3.amazonaws.com/models.huggingface.co/bert/roberta-large-merges.txt -O ${MODEL_DIR}/merges.txt
CUDA_VISIBLE_DEVICES=0,2,3 python models/run_mcqa.py \
--task_name riddleqa \
--model_name_or_path ${MODEL_DIR} \
--do_eval \
--data_dir $DATA_DIR \
--train_file "" --val_file ${DATA_DIR}/test.jsonl \
--test_file "" --prediction_output "" \
--num_choices 5 \
--max_seq_length 100 \
--output_dir /tmp/ \
--per_device_eval_batch_size=6 \
--fp16 --overwrite_output \
--overwrite_cache
``` -->


<!-- 
## ALBERT-xxlarge


### Train
```bash
DATA_DIR=models/data_dir/riddle_sense/
MODEL_DIR=~/riddle_models/albert_large
rm -rf $MODEL_DIR
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
    --greater_is_better \
    --eval_steps 100 \
    --test_file "" --prediction_output "" \
    --num_choices 5 \
    --learning_rate 1e-5 \
    --num_train_epochs 10 \
    --max_seq_length 100 \
    --output_dir ${MODEL_DIR} \
    --per_device_eval_batch_size=1 \
    --per_device_train_batch_size=1 \
    --gradient_accumulation_steps 4 \
    --warmup_steps 100 \
    --fp16 --overwrite_output \
    --overwrite_cache
```

### Test 
```bash   
DATA_DIR=models/data_dir/riddle_sense/
MODEL_DIR=~/riddle_models/albert_large
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python models/run_mcqa.py \
--task_name riddleqa \
--model_name_or_path ${MODEL_DIR} \
--do_eval \
--data_dir $DATA_DIR \
--train_file "" --val_file ${DATA_DIR}/test.jsonl \
--test_file "" --prediction_output "" \
--num_choices 5 \
--max_seq_length 100 \
--output_dir ~/riddle_models/ \
--per_gpu_eval_batch_size=5 \
--fp16 --overwrite_output \
--overwrite_cache
``` -->

# Experiments (Differnt Percentage)
```bash
bash run_by_percentage_roberta.sh > roberta.log
bash run_by_percentage_albert.sh > albert.log
bash run_by_percentage_bert.sh > bert.log
```

# Experiments  (CSQA-->RS) 
```bash
mkdir models/data_dir/csqa_to_rs 
wget https://s3.amazonaws.com/commensenseqa/train_rand_split.jsonl -O models/data_dir/csqa_to_rs/csqa_train.jsonl
wget https://s3.amazonaws.com/commensenseqa/dev_rand_split.jsonl -O models/data_dir/csqa_to_rs/csqa_dev.jsonl 
cp models/data_dir/riddle_sense/train.jsonl models/data_dir/csqa_to_rs/rs_train.jsonl
cat models/data_dir/riddle_sense/train.jsonl models/data_dir/csqa_to_rs/csqa_train.jsonl >  models/data_dir/csqa_to_rs/cat_train.jsonl
cp models/data_dir/riddle_sense/dev.jsonl models/data_dir/csqa_to_rs/rs_dev.jsonl
cp models/data_dir/riddle_sense/test.jsonl models/data_dir/csqa_to_rs/rs_test.jsonl
```

## BERT-Large


### Train
```bash
DATA_DIR=models/data_dir/csqa_to_rs
MODEL_DIR=~/riddle_models/csqa_rs_bert_large
CUDA_VISIBLE_DEVICES=0,1,2,3,  python models/run_mcqa.py \
    --task_name riddleqa \
    --model_name_or_path bert-large-uncased \
    --do_train \
    --do_eval \
    --data_dir $DATA_DIR \
    --train_file ${DATA_DIR}/train.jsonl \
    --val_file ${DATA_DIR}/dev.jsonl \
    --evaluate_during_training \
    --evaluation_strategy steps \
    --load_best_model_at_end \
    --metric_for_best_model eval_acc \
    --greater_is_better \
    --eval_steps 300 \
    --test_file "" --prediction_output "" \
    --num_choices 5 \
    --learning_rate 3e-5 \
    --num_train_epochs 5 \
    --max_seq_length 100 \
    --output_dir ${MODEL_DIR} \
    --per_device_eval_batch_size=4 \
    --per_device_train_batch_size=4 \
    --gradient_accumulation_steps 2 \
    --fp16 --overwrite_output \
    --overwrite_cache
```

### Test 
```bash   
DATA_DIR=models/data_dir/riddle_sense/
MODEL_DIR=~/riddle_models/csqa_rs_bert_large
CUDA_VISIBLE_DEVICES=0,1,2,3 python models/run_mcqa.py \
--task_name riddleqa \
--model_name_or_path ${MODEL_DIR} \
--do_eval \
--data_dir $DATA_DIR \
--train_file "" --val_file ${DATA_DIR}/test.jsonl \
--test_file "" --prediction_output "" \
--num_choices 5 \
--max_seq_length 100 \
--output_dir ~/riddle_models/csqa_rs_ \
--per_gpu_eval_batch_size=6 \
--fp16 --overwrite_output \
--overwrite_cache
```



## RoBERTa-Large


### Train
```bash
DATA_DIR=models/data_dir/csqa_to_rs
MODEL_DIR=~/riddle_models/csqa_rs_roberta_large
CUDA_VISIBLE_DEVICES=4,5,6,7 python models/run_mcqa.py \
    --task_name riddleqa \
    --model_name_or_path roberta-large \
    --do_train \
    --do_eval \
    --data_dir $DATA_DIR \
    --train_file ${DATA_DIR}/train.jsonl \
    --val_file ${DATA_DIR}/dev.jsonl \
    --evaluate_during_training \
    --evaluation_strategy steps \
    --load_best_model_at_end \
    --metric_for_best_model eval_acc \
    --greater_is_better \
    --eval_steps 300 \
    --test_file "" --prediction_output "" \
    --num_choices 5 \
    --learning_rate 1e-5 \
    --num_train_epochs 10 \
    --max_seq_length 100 \
    --output_dir ${MODEL_DIR} \
    --per_device_eval_batch_size=3 \
    --per_device_train_batch_size=3 \
    --gradient_accumulation_steps 4 \
    --warmup_steps 100 \
    --fp16 --overwrite_output \
    --overwrite_cache
```

### Test 
```bash   
DATA_DIR=models/data_dir/csqa_to_rs/
MODEL_DIR=~/riddle_models/csqa_rs_roberta_large
CUDA_VISIBLE_DEVICES=8,9 python models/run_mcqa.py \
--task_name riddleqa \
--model_name_or_path ${MODEL_DIR} \
--do_eval \
--data_dir $DATA_DIR \
--train_file "" --val_file ${DATA_DIR}/test.jsonl \
--test_file "" --prediction_output "" \
--num_choices 5 \
--max_seq_length 100 \
--output_dir ~/riddle_models/csqa_rs_ \
--per_gpu_eval_batch_size=6 \
--fp16 --overwrite_output \
--overwrite_cache
```



## ALBERT-xxlarge


### Train
```bash
DATA_DIR=models/data_dir/riddle_sense
MODEL_DIR=~/riddle_models/riddle_sense_albert_large
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
    --greater_is_better \
    --eval_steps 100 \
    --test_file "" --prediction_output "" \
    --num_choices 5 \
    --learning_rate 1e-5 \
    --num_train_epochs 10 \
    --max_seq_length 100 \
    --output_dir ${MODEL_DIR} \
    --per_device_eval_batch_size=1 \
    --per_device_train_batch_size=1 \
    --gradient_accumulation_steps 4 \
    --warmup_steps 100 \
    --fp16 --overwrite_output \
    --overwrite_cache
```

### Test 
```bash   
DATA_DIR=models/data_dir/csqa_to_rs/
MODEL_DIR=~/riddle_models/csqa_rs_albert_large
CUDA_VISIBLE_DEVICES=8,9 python models/run_mcqa.py \
--task_name riddleqa \
--model_name_or_path ${MODEL_DIR}/ \
--do_eval \
--data_dir $DATA_DIR \
--train_file "" --val_file ${DATA_DIR}/test.jsonl \
--test_file "" --prediction_output "" \
--num_choices 5 \
--max_seq_length 100 \
--output_dir ~/riddle_models/ \
--per_gpu_eval_batch_size=5 \
--fp16 --overwrite_output \
--overwrite_cache
```

