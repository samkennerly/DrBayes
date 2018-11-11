# DrBayes

DrBayes is a [naive Bayes classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier). It is intended as a tutorial for:

- [probabilistic classification](https://en.wikipedia.org/wiki/Probabilistic_classification) with incomplete information
- using [pandas](http://pandas.pydata.org/) to work around missing data
- using CSV and JSON files for table and dictionary storage

## quickstart

1. [Clone this repository](https://help.github.com/articles/cloning-a-repository/) to any folder on your machine.
2. Open a terminal and `cd` to that folder.
3. Enter `python DrBayes.py` to run Python interactively.

DrBayes will:

- ask you several yes/no questions
- diagnose you with one of the conditions in [Symptoms.csv](Symptoms.csv)
- assign you a doctor from [Doctors.json](Doctors.json)

## how it works

Before asking any questions, DrBayes has
[prior beliefs](https://en.wikipedia.org/wiki/Prior_probability)
about your health. After each answer, DrBayes updates its beliefs using
[Bayesian inference](https://en.wikipedia.org/wiki/Bayesian_inference).

Suppose that, among patients who suffer from *Boneitis*,

- 99% report joint pain
- 20% report cold skin
- 5% report numbness
- 1% report multiple shadows

Each of these numbers can be interpreted as a
[conditional probability](https://en.wikipedia.org/wiki/Conditional_probability):

```
P(patient reports "joint pain" | patient has Boneitis) = 0.99
```
Given that you have reported joint pain, the
[likelihood](https://en.wikipedia.org/wiki/Likelihood_function)
that you have Boneitits is:

```
L( you have Boneitits | you reported "joint pain" ) = 0.99
```

The general algorithm after each question is:

```
new_beliefs = old_beliefs * likelihood
new_beliefs /= sum(new_beliefs)
```
The last step ensures that all probabilities sum to 1.

Missing values in Symptoms.csv will be filled with [null values](http://pandas.pydata.org/pandas-docs/stable/missing_data.html) and ignored during calculations. If the patient declines to answer a question, then DrBayes will ignore that question and continue.

