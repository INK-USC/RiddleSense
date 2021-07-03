---
layout: default
title: RiddleSense
nav_order: 1
description: "RiddleSense: Reasoning about Riddle Questions Featuring Linguistic Creativity and Commonsense Knowledge. (ACL21 Findings)"
permalink: /
last_modified_date: Jun 5th 2021
toc_list: true
---


<!-- <link href="http://allfont.net/allfont.css?fonts=agency-fb-bold" rel="stylesheet" type="text/css" /> -->

<style>
@font-face{font-family:agency fb bold;font-style:normal;font-weight:700;src:local('Agency FB Bold'),local('AgencyFB-Bold'),url(http://allfont.net/cache/fonts/agency-fb-bold_cee84847c4ab16cf2b0952d063712724.woff) format('woff'),url(http://allfont.net/cache/fonts/agency-fb-bold_cee84847c4ab16cf2b0952d063712724.ttf) format('truetype')}

p, li{
    font-size: 16px;
} 



.acc{
    font-weight: 700;
    color: green;
    text-align: center;
}

.modelname{
    font-weight: 650;
    text-align: center;
    color: blue;
}

.submitter{
    font-weight: 500;
    text-align: center;
    color: purple;
}

.date{
    font-weight: 500;
    text-align: center;
}

.traindata{
    font-weight: 600;
    text-align: center;
    color: purple;
}
/* #main-content {
    float: center;
    width: auto; } */
</style>


# RiddleSense: Reasoning about Riddle Questions Featuring Linguistic Creativity and Commonsense Knowledge
{: .no_toc style="font-weight: 600; color: #ce210c; font-family: 'Agency FB Bold', arial;"}
✍️ [***Bill Yuchen Lin***](https://yuchenlin.xyz/){: target="blank"}, [***Ziyi Wu***](https://www.linkedin.com/in/ziyiwuxyz/), [***Yichi Yang***](), [***Dong-Ho Lee***](https://danny-lee.info/){: target="blank"}, [***Xiang Ren***](http://www-bcf.usc.edu/~xiangren/){: target="blank"} \
🏢 ***in Proceedings of ACL 2021 Findings***

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
[Leaderboard](#leaderboard){: .btn .btn-red .mr-1 .fs-4 }
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

<!-- ![examples](images/examples.png){: style=""} -->

<div class="1">
    <h3 class="no_toc">- Example 1: I am black when you buy me, red when you use me. When I turn white, you know it's time to trow me away. What am I?</h3>
    <select>
        <option >Select</option>
        <option class="right">A. charcoal</option>
        <option >B. rose flower</option>
        <option >C. ink</option>
        <option >D. fruit</option>
        <option >E. shoe</option>
    </select>
    <div class="check-answer">Select your answer to this riddle!</div>
    <div style="display: none" class="answer" ><span style="font-weight: 500">UnifiedQA's Wrong Prediction:</span> C (ink).  <br>  <span style="font-weight: 600; color: blue">Explanation: </span> Describing multiple conditions 
of a common object. Only charcoal applies to all the descriptions.</div>
</div>

<div class="2">
    <h3 class="no_toc">- Example 2: I have a long tail that I let fly. Every time I go through a gap, I leave a bit of my tail in the trap. What am I?  </h3>
    <select>
        <option >Select</option>
        <option >A. monkey</option>
        <option >B. basketball</option>
        <option >C. fishing pole</option>
        <option >D. comet</option>
        <option class="right">E. needle</option>
    </select>
    <div class="check-answer">Select your answer to this riddle!</div>
    <div style="display: none" class="answer" ><span style="font-weight: 500">UnifiedQA's Wrong Prediction:</span> C (fishing pole). <br> <span style="font-weight: 600; color: blue">Explanation: </span> Describing a common event and involved objects with metaphor. tail → thread; fly → sew; </div>
</div>

<div class="3">
    <h3 class="no_toc">- Example 3: If you take off my skin, I will not cry, but you will. What am I?</h3>
    <select>
        <option >Select</option>
        <option >A. grape</option>
        <option class="right">B. onion</option>
        <option >C. package</option>
        <option >D. plant</option>
        <option >E. body</option>
    </select>
    <div class="check-answer">Select your answer to this riddle!</div>
    <div style="display: none" class="answer" ><span style="font-weight: 500">UnifiedQA's Wrong Prediction:</span> E (body). <br> <span style="font-weight: 600; color: blue">Explanation: </span> Personalization. Cutting onions 
→ taking off my skin. </div>
</div>

<div class="4">
    <h3 class="no_toc">- Example 4: What is that which, though black itself, enlightens the world without burning? </h3>
    <select>
        <option >Select</option>
        <option >A. coal</option>
        <option >B. hole</option>
        <option >C. cd paper</option>
        <option >D. sunlight</option>
        <option class="right">E. ink</option>
    </select>
    <div class="check-answer">Select your answer to this riddle!</div>
    <div style="display: none" class="answer" ><span style="font-weight: 500">UnifiedQA's Wrong Prediction:</span> C (cd paper). <br> <span style="font-weight: 600; color: blue">Explanation: </span> Figure of speech (ink → writing → knowledge → light of wisdom)
+ Counterfactual (without burning) </div>
</div>

<div class="5">
    <h3 class="no_toc">- Example 5: I have hundreds of legs, but I can only lean. What am I?</h3>
    <select>
        <option >Select</option>
        <option >A. chair</option>
        <option >B. sock</option>
        <option >C. pleopod</option>
        <option >D. pant</option>
        <option class="right">E. broom</option>
    </select>
    <div class="check-answer">Select your answer to this riddle!</div>
    <div style="display: none" class="answer" ><span style="font-weight: 500">UnifiedQA's Wrong Prediction:</span> C (pleopod). <br> <span style="font-weight: 600; color: blue">Explanation: </span> Counterfactual (many legs but 
cannot stand) + Metaphor (bristles) </div>
</div>



<script>
    window.onload = function() {

        var selects = document.getElementsByTagName("select")
        console.log(selects.length)
        for (var i = 0; i < selects.length; i++) {

            selects[i].addEventListener("change", function (e) {
                var childrens = e.target.children
                console.log(e.target.parentNode.className)
                for(var j=0;j<childrens.length;j++) {
                    if (childrens[j].className == "right"){
                        var right_index = j
                    }
                }
                var parent = e.target.parentNode.className
                if (e.target.selectedIndex == right_index) {
                    document.getElementsByClassName("check-answer")[parent-1].innerHTML = "Yay! You selected a correct answer! &#128578;"
                    document.getElementsByClassName("check-answer")[parent-1].style.color = "green"
                    document.getElementsByClassName("answer")[parent-1].style.display = "block"
                }else{
                    document.getElementsByClassName("check-answer")[parent-1].innerHTML = "Hmm, it's incorrect. Try again? &#128549;"
                    document.getElementsByClassName("check-answer")[parent-1].style.color = "red"
                }
                
            })


        }
    } 
</script>




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

<table>
<thead>
  <tr>
    <th>Model</th>
    <th>Submitter</th>
    <th>Date</th>
    <th>Training Data</th>
    <th>Acc</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="modelname" style="background-color: #f5f6fa">Humans</td>
    <td class="submitter"  style="background-color: #f5f6fa">-</td>
    <td class="date"  style="background-color: #f5f6fa">-</td>
    <td class="traindata"  style="background-color: #f5f6fa">N/A</td>
    <td class="acc"  style="background-color: #f5f6fa">91.33</td>
  </tr>
  <tr>
    <td class="modelname"><a href="https://arxiv.org/abs/2005.00700" target="_blank">UnifiedQA (T5-3B) </a></td>
    <td class="submitter"><a href="http://inklab.usc.edu" target="_blank">USC-INK</a></td>
    <td class="date">5/30/2021</td>
    <td class="traindata">RS+CSQA</td>
    <td class="acc">68.80</td>
  </tr>
  <tr>
    <td class="modelname"><a href="https://arxiv.org/abs/1909.11942" target="_blank">ALBERT-XXL </a></td>
    <td class="submitter"><a href="http://inklab.usc.edu" target="_blank">USC-INK</a></td>
    <td class="date">5/30/2021</td>
    <td class="traindata">RS+CSQA</td>
    <td class="acc">67.30</td>
  </tr>
  <tr>
    <td class="modelname"><a href="https://arxiv.org/abs/2005.00646" target="_blank">MHGRN (AB-XXL) </a></td>
    <td class="submitter"><a href="http://inklab.usc.edu" target="_blank">USC-INK</a></td>
    <td class="date">5/30/2021</td>
    <td class="traindata">RS+CSQA</td>
    <td class="acc">66.81</td>
  </tr>
  <tr>
    <td class="modelname"><a href="https://arxiv.org/abs/2005.00646" target="_blank">MHGRN (RoBERTa-Large) </a></td>
    <td class="submitter"><a href="http://inklab.usc.edu" target="_blank">USC-INK</a></td>
    <td class="date">5/30/2021</td>
    <td class="traindata">RS+CSQA</td>
    <td class="acc">63.73</td>
  </tr>
  <tr>
    <td class="modelname"><a href="https://arxiv.org/abs/1907.11692" target="_blank">RoBERTa-Large </a></td>
    <td class="submitter"><a href="http://inklab.usc.edu" target="_blank">USC-INK</a></td>
    <td class="date">5/30/2021</td>
    <td class="traindata">RS+CSQA</td>
    <td class="acc">59.82</td>
  </tr>
  <tr>
    <td class="modelname"><a href="https://arxiv.org/abs/1909.02151" target="_blank">KagNet (RoBERTa-Large)</a></td>
    <td class="submitter"><a href="http://inklab.usc.edu" target="_blank">USC-INK</a></td>
    <td class="date">5/30/2021</td>
    <td class="traindata">RS+CSQA</td>
    <td class="acc">59.72</td>
  </tr>
  <tr>
    <td class="modelname"><a href="https://arxiv.org/abs/2005.00700" target="_blank">UnifiedQA (T5-Large)</a></td>
    <td class="submitter"><a href="http://inklab.usc.edu" target="_blank">USC-INK</a></td>
    <td class="date">5/30/2021</td>
    <td class="traindata">RS+CSQA</td>
    <td class="acc">56.57</td>
  </tr>
  <tr>
    <td class="modelname"><a href="https://arxiv.org/abs/1810.04805" target="_blank">BERT-Large</a></td>
    <td class="submitter"><a href="http://inklab.usc.edu" target="_blank">USC-INK</a></td>
    <td class="date">5/30/2021</td>
    <td class="traindata">RS+CSQA</td>
    <td class="acc">54.91</td>
  </tr>
  <tr>
    <td class="modelname"><a href="https://arxiv.org/abs/1810.04805" target="_blank">BERT-Base</a></td>
    <td class="submitter"><a href="http://inklab.usc.edu" target="_blank">USC-INK</a></td>
    <td class="date">5/30/2021</td>
    <td class="traindata">RS+CSQA</td>
    <td class="acc">47.67</td>
  </tr>
  <tr>
    <td class="modelname"  style="background-color: #f5f6fa">Random Guess</td>
    <td class="submitter"  style="background-color: #f5f6fa">-</td>
    <td class="date"  style="background-color: #f5f6fa">-</td>
    <td class="traindata"  style="background-color: #f5f6fa">N/A</td>
    <td class="acc"  style="background-color: #f5f6fa">20.00</td>
  </tr>
</tbody>
</table>

### Submission Guide
{: .no_toc}

This is [***an example submission file***](submission_example.jsonl){: target="_blank"}. Please submit your prediction file and information via [***this form***](https://forms.gle/a3yyoxmgj1FoJpMM7){: target="_blank"}.

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

