# SciBERT-NLI

This is the model [SciBERT](https://github.com/allenai/scibert) [1] fine-tuned on the [SNLI](https://nlp.stanford.edu/projects/snli/) and the [MultiNLI](https://www.nyu.edu/projects/bowman/multinli/) datasets using the [`sentence-transformers` library](https://github.com/UKPLab/sentence-transformers/) to produce universal sentence embeddings [2].

The model uses the original `scivocab` wordpiece vocabulary and was trained using the **average pooling strategy** and a **softmax loss**.

**Base model**: `allenai/scibert-scivocab-cased` from HuggingFace's `AutoModel`.

**Training time**: ~4 hours on the NVIDIA Tesla P100 GPU provided in Kaggle Notebooks.

**Parameters**:

| Parameter        | Value |
|------------------|-------|
| Batch size       | 64    |
| Training steps   | 20000 |
| Warmup steps     | 1450  |
| Lowercasing      | True  |
| Max. Seq. Length | 128   |

**Performances**: The performance was evaluated on the test portion of the [STS dataset](http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark) using Spearman rank correlation and compared to the performances of a general BERT base model obtained with the same procedure to verify their similarity.

| Model                         | Score       |
|-------------------------------|-------------|
| `scibert-nli` (this)          | 74.50       |
| `bert-base-nli-mean-tokens`[3]| 77.12       |

An example usage for similarity-based scientific paper retrieval is provided in the [Covid Papers Browser](https://github.com/gsarti/covid-papers-browser) repository.

**References:**

[1] I. Beltagy et al, [SciBERT: A Pretrained Language Model for Scientific Text](https://www.aclweb.org/anthology/D19-1371/)

[2] A. Conneau et al., [Supervised Learning of Universal Sentence Representations from Natural Language Inference Data](https://www.aclweb.org/anthology/D17-1070/)

[3] N. Reimers et I. Gurevych, [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://www.aclweb.org/anthology/D19-1410/)
