# DrBayes
Example naïve Bayes classifier


## what it does

DrBayes is a Python tutorial for:

- using a [naive Bayes classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
- using the [`pandas`](http://pandas.pydata.org/) package to work with missing data in Python
- storing tables in CSV files and [key-value dictionaries](https://en.wikipedia.org/wiki/Key-value_database) in JSON files


## how to use it

Download these files into the same folder:

- [DrBayes.py](https://github.com/samkennerly/DrBayes/blob/master/DrBayes.py)
- [Doctors.json](https://github.com/samkennerly/DrBayes/blob/master/Doctors.json)
- [Symptoms.csv](https://github.com/samkennerly/DrBayes/blob/master/Symptoms.csv)

Open a terminal, go that folder, and type: python DrBayes.py

DrBayes asks the user several yes/no questions, then attempts to diagnose the user with an illness. For simplicity, it assumes that the user has exactly one of the illnesses listed in Symptoms.csv. To add/subtract illnesses or doctors, modify Symptoms.csv and/or Doctors.json with a text editor.


## how it works

Before asking any questions, DrBayes has [prior beliefs](https://en.wikipedia.org/wiki/Prior_probability) about the user's health. It assumes "Merely A Flesh Wound" with probability 80%, and the remaining 20% is spread equally over all other possible illnesses.

After each question is answered, DrBayes consults Symptoms.csv and updates its beliefs using the rules of [Bayesian inference](https://en.wikipedia.org/wiki/Bayesian_inference). Each row of Symptoms.csv contains (fictional) symptom frequencies reported by (fictional) patients.

For example, consider patients with Boneitis:

* 99% of these patients report joint pain
* 20% report cold skin
* 5% report numbness
* 1% report multiple shadows

Each of these numbers is interpreted as a [conditional probability](https://en.wikipedia.org/wiki/Conditional_probability), e.g.
P( joint pain | Boneitis ) = 0.99

The "likelihood of having Boneitits, given joint pain" is defined:
L( Boneitits | joint pain ) := P( joint pain | Boneitis ) = 0.99

The "likelihood of not having Boneitis, given joint pain" is:
1 - L( Boneitits | joint pain ) = 0.01

The general algorithm after each question is:
* new_beliefs = prior_beliefs * likelihood
* new_beliefs = new_beliefs / sum(new_beliefs)

The last step is  ensure that all probabilities sum to 1.

Missing values in Symptoms.csv will be filled with [null values](http://pandas.pydata.org/pandas-docs/stable/missing_data.html) and ignored during calculations. If the patient declines to answer a question, then DrBayes will ignore that question and continue.

Once DrBayes has diagnosed the user, it will recommend a (fictional) doctor. Doctors and their specialties are stored as a dictionary in Doctors.json with doctor names as keys and their specialties as values. DrBayes performs a reverse search of the dictionary: given a value, find all keys with that value.
