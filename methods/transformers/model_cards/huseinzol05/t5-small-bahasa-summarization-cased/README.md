---
language: ms
---

# Bahasa T5 Summarization Model

Finetuned T5 small summarization model for Malay and Indonesian. 

## Finetuning Corpus

`t5-small-bahasa-summarization-cased` model was finetuned on multiple summarization dataset. Below is list of tasks we trained on,

1. [Translated CNN News](https://github.com/huseinzol05/Malay-Dataset#cnn-news)
2. [Translated Gigawords](https://github.com/huseinzol05/Malay-Dataset#gigawords)
3. [Translated Multinews](https://github.com/huseinzol05/Malay-Dataset#multinews)

## Finetuning details

- This model was trained using Malaya T5's github [repository](https://github.com/huseinzol05/Malaya/tree/master/pretrained-model/t5) on v3-8 TPU using small size.
- All steps can reproduce from here, [Malaya/session/summarization](https://github.com/huseinzol05/Malaya/tree/master/session/summarization).

## Load Finetuned Model

You can use this model by installing `torch` or `tensorflow` and Huggingface library `transformers`. And you can use it directly by initializing it like this:  

```python
from transformers import T5Tokenizer, T5Model

tokenizer = T5Tokenizer.from_pretrained('huseinzol05/t5-small-bahasa-summarization-cased')
model = T5ForConditionalGeneration.from_pretrained('huseinzol05/t5-small-bahasa-summarization-cased')
```

## Example using T5ForConditionalGeneration

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained('huseinzol05/t5-small-bahasa-summarization-cased')
model = T5ForConditionalGeneration.from_pretrained('huseinzol05/t5-small-bahasa-summarization-cased')

# https://www.hmetro.com.my/mutakhir/2020/05/580438/peletakan-jawatan-tun-m-ditolak-bukan-lagi-isu
# original title, Peletakan jawatan Tun M ditolak, bukan lagi isu
string = 'PELETAKAN jawatan Tun Dr Mahathir Mohamad sebagai Pengerusi Parti Pribumi Bersatu Malaysia (Bersatu) ditolak di dalam mesyuarat khas Majlis Pimpinan Tertinggi (MPT) pada 24 Februari lalu. Justeru, tidak timbul soal peletakan jawatan itu sah atau tidak kerana ia sudah pun diputuskan pada peringkat parti yang dipersetujui semua termasuk Presiden, Tan Sri Muhyiddin Yassin. Bekas Setiausaha Agung Bersatu Datuk Marzuki Yahya berkata, pada mesyuarat itu MPT sebulat suara menolak peletakan jawatan Dr Mahathir. "Jadi ini agak berlawanan dengan keputusan yang kita sudah buat. Saya tak faham bagaimana Jabatan Pendaftar Pertubuhan Malaysia (JPPM) kata peletakan jawatan itu sah sedangkan kita sudah buat keputusan di dalam mesyuarat, bukan seorang dua yang buat keputusan. "Semua keputusan mesti dibuat melalui parti. Walau apa juga perbincangan dibuat di luar daripada keputusan mesyuarat, ini bukan keputusan parti. "Apa locus standy yang ada pada Setiausaha Kerja untuk membawa perkara ini kepada JPPM. Seharusnya ia dibawa kepada Setiausaha Agung sebagai pentadbir kepada parti," katanya kepada Harian Metro. Beliau mengulas laporan media tempatan hari ini mengenai pengesahan JPPM bahawa Dr Mahathir tidak lagi menjadi Pengerusi Bersatu berikutan peletakan jawatannya di tengah-tengah pergolakan politik pada akhir Februari adalah sah. Laporan itu juga menyatakan, kedudukan Muhyiddin Yassin memangku jawatan itu juga sah. Menurutnya, memang betul Dr Mahathir menghantar surat peletakan jawatan, tetapi ditolak oleh MPT. "Fasal yang disebut itu terpakai sekiranya berhenti atau diberhentikan, tetapi ini mesyuarat sudah menolak," katanya. Marzuki turut mempersoal kenyataan media yang dibuat beberapa pimpinan parti itu hari ini yang menyatakan sokongan kepada Perikatan Nasional. "Kenyataan media bukanlah keputusan rasmi. Walaupun kita buat 1,000 kenyataan sekali pun ia tetap tidak merubah keputusan yang sudah dibuat di dalam mesyuarat. Kita catat di dalam minit apa yang berlaku di dalam mesyuarat," katanya.'

# https://huggingface.co/blog/how-to-generate
# generate summary
input_ids = tokenizer.encode(f'ringkasan: {string}', return_tensors = 'pt')
outputs = model.generate(
    input_ids,
    do_sample = True,
    temperature = 0.8,
    top_k = 50,
    top_p = 0.95,
    max_length = 300,
    num_return_sequences = 3,
)

for i, sample_output in enumerate(outputs):
    print(
        '{}: {}'.format(
            i, tokenizer.decode(sample_output, skip_special_tokens = True)
        )
    )

# generate news title
input_ids = tokenizer.encode(f'tajuk: {string}', return_tensors = 'pt')
outputs = model.generate(
    input_ids,
    do_sample = True,
    temperature = 0.8,
    top_k = 50,
    top_p = 0.95,
    max_length = 300,
    num_return_sequences = 3,
)

for i, sample_output in enumerate(outputs):
    print(
        '{}: {}'.format(
            i, tokenizer.decode(sample_output, skip_special_tokens = True)
        )
    )
```

Output is,

```
0: Pengerusi Bersatu Bersatu menafikan peletakan jawatan dalam mesyuarat khas Majlis Pimpinan Tertinggi. Tidak timbul isu peletakan jawatan itu sah atau tidak kerana ia sudah diputuskan di peringkat parti. Kenyataan media yang dibuat oleh pemimpin parti hari ini menyokong Perikatan Nasional
1: Tiada keputusan kerana ia sudah diputuskan pada peringkat parti, Marzuki berkata. Pejabat rasmi parti menolak peletakan jawatan Dr M, dengan mengatakan ia adalah keputusan. Kedudukan Muhyiddin memangku jawatan itu juga sah, katanya
2: Tiada peletakan jawatan Dr Mahathir dalam mesyuarat khas MPT pada 24 Februari. Ketua parti menolak peletakan jawatan itu. Tidak timbul isu peletakan jawatan itu sah atau tidak, katanya

0: Tiada peletakan jawatan Tun M dalam mesyuarat khas
1: ???Tidak timbul peletakan jawatan Tun M???
2: Tidak timbul isu peletakan jawatan Tun M di mesyuarat khas
```

## Result

We found out using original Tensorflow implementation gives better results, check it at https://malaya.readthedocs.io/en/latest/Abstractive.html#generate-ringkasan

## Acknowledgement

Thanks to [Im Big](https://www.facebook.com/imbigofficial/), [LigBlou](https://www.facebook.com/ligblou), [Mesolitica](https://mesolitica.com/) and [KeyReply](https://www.keyreply.com/) for sponsoring AWS, Google and GPU clouds to train T5 for Bahasa. 
