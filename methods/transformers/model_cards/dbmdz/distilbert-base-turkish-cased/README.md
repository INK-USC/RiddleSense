---
language: tr
license: mit
---

# 🤗 + 📚 dbmdz Distilled Turkish BERT model

In this repository the MDZ Digital Library team (dbmdz) at the Bavarian State
Library open sources a (cased) distilled model for Turkish 🎉

# 🇹🇷 DistilBERTurk

DistilBERTurk is a community-driven cased distilled BERT model for Turkish.

DistilBERTurk was trained on 7GB of the original training data that was used
for training [BERTurk](https://github.com/stefan-it/turkish-bert/tree/master#stats),
using the cased version of BERTurk as teacher model.

*DistilBERTurk* was trained with the official Hugging Face implementation from
[here](https://github.com/huggingface/transformers/tree/master/examples/distillation)
for 5 days on 4 RTX 2080 TI.

More details about distillation can be found in the
["DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter"](https://arxiv.org/abs/1910.01108)
paper by Sanh et al. (2019).

## Model weights

Currently only PyTorch-[Transformers](https://github.com/huggingface/transformers)
compatible weights are available. If you need access to TensorFlow checkpoints,
please raise an issue in the [BERTurk](https://github.com/stefan-it/turkish-bert) repository!

| Model                             | Downloads
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------
| `dbmdz/distilbert-base-turkish-cased`   | [`config.json`](https://cdn.huggingface.co/dbmdz/distilbert-base-turkish-cased/config.json) • [`pytorch_model.bin`](https://cdn.huggingface.co/dbmdz/distilbert-base-turkish-cased/pytorch_model.bin) • [`vocab.txt`](https://cdn.huggingface.co/dbmdz/distilbert-base-turkish-cased/vocab.txt)

## Usage

With Transformers >= 2.3 our DistilBERTurk model can be loaded like:

```python
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("dbmdz/distilbert-base-turkish-cased")
model = AutoModel.from_pretrained("dbmdz/distilbert-base-turkish-cased")
```

## Results

For results on PoS tagging or NER tasks, please refer to
[this repository](https://github.com/stefan-it/turkish-bert).

For PoS tagging, DistilBERTurk outperforms the 24-layer XLM-RoBERTa model.

The overall performance difference between DistilBERTurk and the original
(teacher) BERTurk model is ~1.18%.

# Huggingface model hub

All models are available on the [Huggingface model hub](https://huggingface.co/dbmdz).

# Contact (Bugs, Feedback, Contribution and more)

For questions about our BERT models just open an issue
[here](https://github.com/dbmdz/berts/issues/new) 🤗

# Acknowledgments

Thanks to [Kemal Oflazer](http://www.andrew.cmu.edu/user/ko/) for providing us
additional large corpora for Turkish. Many thanks to Reyyan Yeniterzi for providing
us the Turkish NER dataset for evaluation.

Research supported with Cloud TPUs from Google's TensorFlow Research Cloud (TFRC).
Thanks for providing access to the TFRC ❤️

Thanks to the generous support from the [Hugging Face](https://huggingface.co/) team,
it is possible to download both cased and uncased models from their S3 storage 🤗
