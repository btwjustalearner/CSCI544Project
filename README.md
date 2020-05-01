# CSCI544Project

Proposal: https://docs.google.com/document/d/16tscH3wKUSsWF5yoF2ZXcvFu0yUD-Tm2VUcgOu9D0g0/edit

Article selection: https://docs.google.com/document/d/1t1u2e_t6WTmYtB2iXcOHjl8KCL0EsM_6J9CxGoJnyRY/edit

Paper presentation slides: https://docs.google.com/presentation/d/1FTTzCuCzrpE6R6Btt-teqgcOB_pr-6bxHAlXCCdqfzA/edit#slide=id.p

English news zip file: https://drive.google.com/file/d/1rD3AL7AYAHanqIO7G2Kgn9ByuQLBEHJR/view?usp=sharing

Final report: https://www.overleaf.com/project/5ea4f006dceffc0001b99e40



4/7 meeting:

Yan:
Logistic regression baseline model
traindata0401.csv 0/1 converting
time series rerun
data combination to new train/test datasets
voting results combining

Zhean:
data cleaning and summary for Chinese/English train/test

Haomeng:
Stock data collecting for Chinese/English train/test


Keyu:
new NLP models

poster:
https://www.overleaf.com/project/5e97764a82e35b00012cbc12


4/21

Next steps:

CNN segmentation

Interpret

questions and test hypothesis

hybrid good models only

English worse than Chinese?

1) Different market

2) news sampling

3) news length

Segmentation outperforms char-based?

Only true for naive bayes?

1) sparsity

2) out of vocabulary

3) overfitting

NB outperforms CNN?


Yan:

nb with random 01

0.5 f1

hybrid good models

ZH: LR(nbseg+cnnnoseg) f1 0.767 coef: [1.48158467, 0.67093084]

EN: LR(nbseg+cnn) f1 0.643 coef: [0.73046022, 0.28719831]

ZH: LR(nbseg+fasttext) f1 0.753 coef: [0.97050265, 1.63139597]

EN: LR(nbseg+fasttext) f1 0.626 coef: [ 0.97564551, -0.19412174]

Haomeng:

CNN seg

ZH > EN?


Keyu:

fast char-based

char-based > seg?


Zhean:

final report


