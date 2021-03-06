---
language: ms
---

# Bahasa GPT2 Model

Pretrained GPT2 345M model for Malay.

## Pretraining Corpus

`gpt2-345M-bahasa-cased` model was pretrained on ~0.9 Billion words. We trained on standard language structure only, and below is list of data we trained on,

1. [dumping wikipedia](https://github.com/huseinzol05/Malaya-Dataset#wikipedia-1).
2. [local news](https://github.com/huseinzol05/Malaya-Dataset#public-news).
3. [local parliament text](https://github.com/huseinzol05/Malaya-Dataset#parliament).
4. [local singlish/manglish text](https://github.com/huseinzol05/Malaya-Dataset#singlish-text).
5. [IIUM Confession](https://github.com/huseinzol05/Malaya-Dataset#iium-confession).
6. [Wattpad](https://github.com/huseinzol05/Malaya-Dataset#wattpad).
7. [Academia PDF](https://github.com/huseinzol05/Malaya-Dataset#academia-pdf).
8. [Common-Crawl](https://github.com/huseinzol05/malaya-dataset#common-crawl).

Preprocessing steps can reproduce from here, [Malaya/pretrained-model/preprocess](https://github.com/huseinzol05/Malaya/tree/master/pretrained-model/preprocess).

## Pretraining details

- This model was trained using GPT2's github [repository](https://github.com/openai/gpt-2) on a V3-8 TPU.
- All steps can reproduce from here, [Malaya/pretrained-model/gpt2](https://github.com/huseinzol05/Malaya/tree/master/pretrained-model/gpt2).

## Load Pretrained Model

You can use this model by installing `torch` or `tensorflow` and Huggingface library `transformers`. And you can use it directly by initializing it like this:  

```python
from transformers import GPT2Tokenizer, GPT2Model

model = GPT2Model.from_pretrained('huseinzol05/gpt2-345M-bahasa-cased')
tokenizer = GPT2Tokenizer.from_pretrained(
    'huseinzol05/gpt2-345M-bahasa-cased',
)
```

## Example using GPT2LMHeadModel

```python
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('huseinzol05/gpt2-345M-bahasa-cased')
model = GPT2LMHeadModel.from_pretrained(
    'huseinzol05/gpt2-345M-bahasa-cased', pad_token_id = tokenizer.eos_token_id
)

input_ids = tokenizer.encode(
    'penat bak hang, macam ni aku takmau kerja dah', return_tensors = 'pt'
)
sample_outputs = model.generate(
    input_ids,
    do_sample = True,
    max_length = 50,
    top_k = 50,
    top_p = 0.95,
    num_return_sequences = 3,
)

print('Output:\n' + 100 * '-')
for i, sample_output in enumerate(sample_outputs):
    print(
        '{}: {}'.format(
            i, tokenizer.decode(sample_output, skip_special_tokens = True)
        )
    )
```

Output is,

```text
Output:
----------------------------------------------------------------------------------------------------
0: penat bak hang, macam ni aku takmau kerja dah dekat 2,3 jam.
Aku harap aku dapat berjimat banyak.
Ini pun masa kerja, bila dah kerja jadi satu.
Aku buat kerja ni la.
Aku memang kalau ada
1: penat bak hang, macam ni aku takmau kerja dah.
Tapi nak buat macam mana kan, aku tolong bentang tugas.
Dan, memang sangat-sangat tak mahu buat kerja sekarang ni.
Aku pun suka sangat kerja di luar bandar
2: penat bak hang, macam ni aku takmau kerja dah pun.
Takpa nak buat kerja-kerja sampingan, baru boleh dapat hadiah pulak.
Ni la tempat paling best bila duduk di restoran yang ada pekena kopi.
Cumanya
```
