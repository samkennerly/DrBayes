# DrBayes

Example [naive Bayes classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier).

DrBayes is a tutorial for:

- [probabilistic classification](https://en.wikipedia.org/wiki/Probabilistic_classification) with incomplete information
- using [pandas](http://pandas.pydata.org/) to work around missing data
- using CSV and JSON files for table and dictionary storage

## quickstart

Download these files into the same folder (or use [git clone](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)):

- [DrBayes.py](https://github.com/samkennerly/DrBayes/blob/master/DrBayes.py)
- [Doctors.json](https://github.com/samkennerly/DrBayes/blob/master/Doctors.json)
- [Symptoms.csv](https://github.com/samkennerly/DrBayes/blob/master/Symptoms.csv)

Open a terminal, go that folder, and enter

```
python DrBayes.py
```
DrBayes will then:
- ask you several yes/no questions
- diagnose you with one of the conditions in [Symptoms.csv](Symptoms.csv)
- assign you a doctor from [Doctors.json](Doctors.json)

## how it works

Before asking any questions, DrBayes has
[prior beliefs](https://en.wikipedia.org/wiki/Prior_probability)
about your health. After each answer, DrBayes updates its beliefs using
[Bayesian inference](https://en.wikipedia.org/wiki/Bayesian_inference).
For example, consider patients with Boneitis:

* 99% report joint pain
* 20% report cold skin
* 5% report numbness
* 1% report multiple shadows

Each of these numbers can be interpreted as a
[conditional probability](https://en.wikipedia.org/wiki/Conditional_probability):
```
P( joint pain | Boneitis ) = 0.99
```
Given that you have joint pain, the
[likelihood](https://en.wikipedia.org/wiki/Likelihood_function)
that you have Boneitits is:
```
L( Boneitits | joint pain ) = P( joint pain | Boneitis ) = 0.99
```

The general algorithm after each question is:
* new_beliefs = prior_beliefs * likelihood
* new_beliefs = new_beliefs / sum(new_beliefs)

The last step ensures that all probabilities sum to 1.

Missing values in Symptoms.csv will be filled with [null values](http://pandas.pydata.org/pandas-docs/stable/missing_data.html) and ignored during calculations. If the patient declines to answer a question, then DrBayes will ignore that question and continue.

Once DrBayes has diagnosed the user, it will recommend a (fictional) doctor. Doctors and their specialties are stored as a dictionary in Doctors.json with doctor names as keys and their specialties as values. DrBayes performs a reverse search of the dictionary: given a value, find all keys with that value.
