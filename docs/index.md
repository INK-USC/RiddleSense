---
layout: default
title: RiddleSense
nav_order: 1
description: "RiddleSense: Reasoning about Riddle Questions Featuring Linguistic Creativity and Commonsense Knowledge. (ACL21 Findings)"
permalink: /
last_modified_date: Jun 5th 2021
toc_list: true
---




<style>
p, li{
    font-size: 16px;
} 
/* #main-content {
    float: center;
    width: auto; } */
</style>


# RiddleSense: Reasoning about Riddle Questions Featuring Linguistic Creativity and Commonsense Knowledge (ACL 2021 Findings)
{: .no_toc}
---

> _"The essence of a riddle is to express true facts under impossible combinations."_  — ***Aristotle***, ***Poetics*** (350 BCE)
{: .fs-7 .fw-500 .text-blue-300 }

---
![authors](images/authors.png){: style="border: 0px solid red"}

---

## Quick Links
{: .no_toc}
<!-- {: .fs-7 .fw-700 .text-blue-300 } -->
<span class="fs-4">
[Paper](riddlesense_acl21.pdf){: target="_blank" .btn .btn-green .mr-1 .fs-4}
[Github](https://github.com/INK-USC/RiddleSense/){: target="_blank" .btn .btn-purple .mr-1 .fs-4 }
[Dataset](https://forms.gle/iWdsgN44TeoXW19e6){: target="_blank" .btn .btn-blue .mr-1 .fs-4 }
<!-- [Download MickeyCorpus](https://forms.gle/fCxN1YAyqKpQ4cXNA){: target="_blank" .btn .btn-blue .mr-1 .fs-3 }
[Download X-CSR Datasets](https://forms.gle/gVCNgVXr1tyYkDya9){: target="_blank" .btn .btn-blue .mr-1 .fs-3 } -->
<!-- [Video](https://mega.nz/file/5SpQjJKS#J82pfZVDzy3r4aWdNF4R6O8EP5gsepbY20vYihANfgE){: target="_blank" .btn .btn-blue .mr-1 .fs-3 }
[Slides](/opencsr_naacl_slides.pptx){: target="_blank" .btn .btn-red .mr-1 .fs-3 } -->
</span> 
<!-- 
[***Intro***](#intro){: .mr-1 .fs-5} 
[***Leaderboard***](#leaderboard){:  .mr-1 .fs-5 } 
[***Citation***](#citation){: mr-1 .fs-5 } -->
<!-- - TOC
{:toc} -->

<!-- [Download MickeyCorpus](https://forms.gle/fCxN1YAyqKpQ4cXNA){: target="_blank" .btn .btn-blue .mr-1 .fs-3 }
[Download X-CSR Datasets](https://forms.gle/gVCNgVXr1tyYkDya9){: target="_blank" .btn .btn-blue .mr-1 .fs-3 } -->
<!-- [Video](https://mega.nz/file/5SpQjJKS#J82pfZVDzy3r4aWdNF4R6O8EP5gsepbY20vYihANfgE){: target="_blank" .btn .btn-blue .mr-1 .fs-3 }
[Slides](/opencsr_naacl_slides.pptx){: target="_blank" .btn .btn-red .mr-1 .fs-3 } -->
---
 
## Abstract
<!-- This is the project site for the paper, [_Differentiable Cross-Lingual Commonsense Reasoning_](https://www.aclweb.org/anthology/2021.naacl-main.366/){: target="_blank"}, by [_Bill Yuchen Lin_](https://yuchenlin.xyz/){: target="_blank"}, [_Haitian Sun_](https://scholar.google.com/citations?user=opSHsTQAAAAJ&hl=en){: target="_blank"}, [_Bhuwan Dhingra_](http://www.cs.cmu.edu/~bdhingra/){: target="_blank"}, [_Manzil Zaheer_](https://scholar.google.com/citations?user=A33FhJMAAAAJ&hl=en){: target="_blank"}, [_Xiang Ren_](http://ink-ron.usc.edu/xiangren/){: target="_blank"}, and [_William W. Cohen_](https://wwcohen.github.io/){: target="_blank"}, in Proc. of [*NAACL 2021*](https://2021.naacl.org/){: target="_blank"}. 
This is a joint work by Google Research and USC. -->

 
![intro](images/riddle_intro.png){: style="border: 2px solid black"}
<!-- ##  --> 
<!-- ***Abstract.***{: .text-red-100}  -->

***Question: I have five fingers but I am not alive.  What am I?  Answer: a glove.***

Answering such a riddle-style question is a challenging cognitive process, in that it requires complex commonsense reasoning abilities, an understanding of figurative language, and counterfactual reasoning skills, which are all important abilities for advanced natural language understanding (NLU).
However, there is currently no dedicated datasets aiming to test these abilities. Herein, we present RiddleSense, a new multiple-choice question answering task,
which comes with the first large dataset (5.7k examples) for answering riddle-style commonsense questions. 
We systematically evaluate a wide range of models over the challenge, and point out that there is a large gap between the best-supervised model and human performance --- suggesting intriguing future research in the direction of higher-order commonsense reasoning and linguistic creativity towards building advanced NLU systems. 

## Examples

## Dataset Format

Please download our dataset by filling the [***form***](https://forms.gle/iWdsgN44TeoXW19e6){: target="_blank"} here and the link will show up once you read the disclaimer and submit it. There are five files as follows:

1. `rs_train.jsonl` (3,510 lines)
    - The training data of RiddleSense.
1. `csqa_train.jsonl` (9,741 lines)
    - The training data of CommonsenseQA.
1. `csqa_rs_train.jsonl` (13,251 lines)
    - The training of of CommonsenseQA + RiddleSense, i.e., the combination of both.
1. `rs_dev.jsonl` (1,021 lines)
    - The development data of RiddleSense.
1. `rs_test_hidden.jsonl` (1,184 lines)
    - The test data of RiddleSense, where the truth answers are hidden.

```json
{   # a particular line in our jsonl file
    "id": "c1235zcx90023230",
    "question": {
        "stem": "My life can be measured in hours. I serve by being devoured. Thin, I am quick. Fat, I am slow. Wind is my foe. What am I?",    # The riddle question.
        "choices": [
            {"label": "A", "text": "paper"},
            {"label": "B", "text": "candle"},   # the correct answer
            {"label": "C", "text": "lamp"},
            {"label": "D", "text": "clock"},
            {"label": "E", "text": "worm"}
        ]
    },
    "answerKey": "B"    # this will be "hidden" in the test data.
}
```


## Leaderboard




## Citation

```bibtex
@inproceedings{lin-etal-2021-riddlesense,
    title = "RiddleSense: Reasoning about Riddle Questions Featuring Linguistic Creativity and Commonsense Knowledge",
    author = "Lin, Bill Yuchen and Wu, Ziyi and Yang, Yichi and Lee, Dong-Ho and Ren, Xiang",
    booktitle = "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL-IJCNLP 2021): Findings",
    year = "2021",
    note={to appear}
}
``` 
{: .fs-4}
<!-- 
[The site is under development. Please email [***yuchen.lin@usc.edu***] if you have any questions.](){: .btn .btn-red .fs-4 target="_blank"} -->

