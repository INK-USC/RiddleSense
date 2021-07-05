## UnifiedQA

### Installation
```bash
conda create --name t5-stable python=3.7
conda activate t5-stable

pip install torch==1.7.0+cu101 torchvision==0.8.1+cu101 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install pytorch-lightning==0.9.0

git clone https://github.com/huggingface/transformers
cd transformers
pip install .
```

### Test (Zero-Shot : base)
```bash
python models/t5/predict.py \
--data_dir data_dir/ \
--model_name_or_path allenai/unifiedqa-t5-base \
--output_dir models/t5/outputs/unifiedqa-base-zeroshot \
--max_seq_length 128 \
--eval_batch_size 4 \
--model_parallel True
```
```bash
python models/t5/eval.py \
--ground_truth_labels_dir data_dir/ \
--predicted_labels_dir models/t5/outputs/unifiedqa-base-zeroshot
```

### Test (Zero-Shot : large)
```bash
python models/t5/predict.py \
--data_dir data_dir/ \
--model_name_or_path allenai/unifiedqa-t5-large \
--output_dir models/t5/outputs/unifiedqa-large-zeroshot \
--max_seq_length 128 \
--eval_batch_size 4 \
--model_parallel True
```
```bash
python models/t5/eval.py \
--ground_truth_labels_dir data_dir/ \
--predicted_labels_dir models/t5/outputs/unifiedqa-large-zeroshot
```

### Test (Zero-Shot : 3b)
```bash
python models/t5/predict.py \
--data_dir data_dir/ \
--model_name_or_path allenai/unifiedqa-t5-3b \
--output_dir models/t5/outputs/unifiedqa-3b-zeroshot \
--max_seq_length 128 \
--eval_batch_size 4 \
--model_parallel True
```
```bash
python models/t5/eval.py \
--ground_truth_labels_dir data_dir/ \
--predicted_labels_dir models/t5/outputs/unifiedqa-3b-zeroshot
```

### Test (Zero-Shot : 11b)
```bash
python models/t5/predict.py \
--data_dir data_dir/ \
--model_name_or_path allenai/unifiedqa-t5-11b \
--output_dir models/t5/outputs/unifiedqa-11b-zeroshot \
--max_seq_length 128 \
--eval_batch_size 4 \
--model_parallel True
```
```bash
python models/t5/eval.py \
--ground_truth_labels_dir data_dir/ \
--predicted_labels_dir models/t5/outputs/unifiedqa-11b-zeroshot
```

### Train (base)
```bash
python models/t5/finetune.py \
--data_dir data_dir/ \
--output_dir models/t5/checkpoints/unifiedqa-base \
--model_name_or_path allenai/unifiedqa-t5-base \
--tokenizer_name_or_path allenai/unifiedqa-t5-base \
--learning_rate 3e-4 \
--max_seq_length 128 \
--train_batch_size 16 \
--gradient_accumulation_steps 4 \
--model_parallel True
```

### Test (From Fine-tuned base)
```bash
python models/t5/predict.py \
--data_dir data_dir/ \
--tokenizer_name_or_path allenai/unifiedqa-t5-base \
--checkpoint_dir models/t5/checkpoints/unifiedqa-base \
--output_dir models/t5/outputs/unifiedqa-base-finetune \
--max_seq_length 128 \
--eval_batch_size 4 \
--model_parallel True
```

```bash
python models/t5/eval.py \
--ground_truth_labels_dir data_dir/ \
--predicted_labels_dir models/t5/outputs/unifiedqa-base-finetune
```

### Train (large)
```bash
sbatch models/t5/finetune_large.sh
```
```bash
python models/t5/finetune.py \
--data_dir data_dir/ \
--output_dir models/t5/checkpoints/unifiedqa-large \
--model_name_or_path allenai/unifiedqa-t5-large \
--tokenizer_name_or_path allenai/unifiedqa-t5-large \
--learning_rate 3e-4 \
--max_seq_length 128 \
--train_batch_size 16 \
--gradient_accumulation_steps 4 \
--model_parallel True
```
### Test (From Fine-tuned large)
```bash
python models/t5/predict.py \
--data_dir data_dir/ \
--tokenizer_name_or_path allenai/unifiedqa-t5-large \
--checkpoint_dir models/t5/checkpoints/unifiedqa-large \
--output_dir models/t5/outputs/unifiedqa-large-finetune \
--max_seq_length 128 \
--eval_batch_size 4 \
--model_parallel True
```

```bash
python models/t5/eval.py \
--ground_truth_labels_dir data_dir/ \
--predicted_labels_dir models/t5/outputs/unifiedqa-large-finetune
```

### Train (3B)
```bash
python models/t5/finetune.py \
--data_dir data_dir/ \
--output_dir models/t5/checkpoints/unifiedqa-3b \
--model_name_or_path allenai/unifiedqa-t5-3b \
--tokenizer_name_or_path allenai/unifiedqa-t5-3b \
--learning_rate 3e-4 \
--max_seq_length 128 \
--train_batch_size 16 \
--gradient_accumulation_steps 4 \
--model_parallel True
```

### Test (From Fine-tuned 3B)
```bash
python models/t5/predict.py \
--data_dir data_dir/ \
--tokenizer_name_or_path allenai/unifiedqa-t5-3b \
--checkpoint_dir models/t5/checkpoints/unifiedqa-3b \
--output_dir models/t5/outputs/unifiedqa-3b-finetune \
--max_seq_length 128 \
--eval_batch_size 4 \
--model_parallel True
```

```bash
python models/t5/eval.py \
--ground_truth_labels_dir data_dir/ \
--predicted_labels_dir models/t5/outputs/unifiedqa-3b-finetune
```
