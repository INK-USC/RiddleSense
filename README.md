
# RiddleSense: Reasoning about Riddle Questions Featuring Linguistic Creativity and Commonsense Knowledge


Please check our project website at: [***https://inklab.usc.edu/RiddleSense/***](https://inklab.usc.edu/RiddleSense/).
 
## Abstract 

 
![intro](https://inklab.usc.edu/RiddleSense/images/riddle_intro.png)

***Question: I have five fingers but I am not alive.  What am I?  Answer: a glove.***

Answering such a riddle-style question is a challenging cognitive process, in that it requires complex commonsense reasoning abilities, an understanding of figurative language, and counterfactual reasoning skills, which are all important abilities for advanced natural language understanding (NLU).
However, there is currently no dedicated datasets aiming to test these abilities. Herein, we present RiddleSense, a new multiple-choice question answering task,
which comes with the first large dataset (5.7k examples) for answering riddle-style commonsense questions. 
We systematically evaluate a wide range of models over the challenge, and point out that there is a large gap between the best-supervised model and human performance --- suggesting intriguing future research in the direction of higher-order commonsense reasoning and linguistic creativity towards building advanced NLU systems. 



## Methods 
Here in this repo, we mainly present the baseline methods that we used in our experiments.

### Installation


```bash
conda create --name riddlesense python=3.7
conda activate riddlesense
pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html

### git clone https://github.com/huggingface/transformers

cd transformers
pip install .
pip install tensorboardX
pip install absl-py

```

```bash 
# if you need to use fp16 for speeding up.
git clone https://github.com/NVIDIA/apex
cd apex
pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
```

### Experiments

Please check the following bash files for fine-tuning different pre-trained LMs on the RiddleSense dataset.
Note that you need to manually change the `rs_train.jsonl` to `csqa_rs_train.jsonl` if you want to use the combination of csqa+riddlesense as the training data.
```bash
bash models/scripts/train_bert_base.sh
bash models/scripts/train_bert_large.sh
bash models/scripts/train_roberta_large.sh
bash models/scripts/train_albert_xxlarge.sh
```

For fine-tuning UnifiedQA models, please refer to our instruction here: [methods/t5/README.md](methods/t5/README.md).

