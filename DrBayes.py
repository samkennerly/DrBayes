#!/usr/bin/env python
'''
DrBayes is a simple example of a naive Bayes classifier.
It attempts to guess a patient's illness by asking yes/no questions.
To run this program, open a terminal and type: python DrBayes.py
Made and tested using Anaconda 4.2.0 (Python 3.5.2).
'''
import pandas as pd
import json


''' Get data from files '''

# Get DataFrame of symptom frequencies from CSV
SymptomTable 	= pd.read_csv('Symptoms.csv')
SymptomTable	= SymptomTable.set_index('illness')
all_illnesses 	= SymptomTable.index
all_symptoms 	= SymptomTable.columns

# Get dictionary of {doctor:specialties} from JSON
with open('Doctors.json') as doctor_file:
	Doctors = json.load(doctor_file)


''' Diagnose the patient and recommend a doctor '''

# At first, Dr. Bayes believes it's probably merely a flesh wound.
# All other possible illnesses are considered equally probable.
normalizer 	= 0.2 / (len(all_illnesses)-1)
Prob 		= pd.Series(normalizer,index=all_illnesses)
Prob.loc['Merely A Flesh Wound'] = 0.8

# Query the patient and update the doctor's beliefs accordingly
print( "My name is Dr. Bayes, and I'm going to ask you a bunch of questions." )
print( "Please enter Y for yes or N for no.\n" )
for symptom in all_symptoms:
	
	# If no answer, then skip to next symptom.
	yn = input("Are you experiencing unusual %s? " % symptom)
	if yn.upper() == 'Y':
		has_symptom = True
	elif yn.upper() == 'N':
		has_symptom = False
	else:
		print( "I'm sorry, I didn't understand your answer." )
		continue
		
	# Update the doctor's beliefs
	likelihood 	= SymptomTable[symptom]
	fValid 		= likelihood.notnull()
	if has_symptom:
		Prob[fValid] *= likelihood
	else:
		Prob[fValid] *= (1-likelihood)
		
	# Remember to normalize the distribution
	Prob /= Prob.sum()
		
# Show the most probable illnesses
print( "\nI believe these illnesses are consistent with your symptoms:" )
Prob = Prob.sort_values(ascending=False)
for illness in Prob.index:
	pct = 100 * Prob.loc[illness].round(4)
	if pct > 10:
		print( "%02d %% \t %s" % (pct,illness) )
		

''' Recommend doctors '''

# This is a crude "reverse dictionary lookup."
diagnosis = Prob.idxmax()
print( "\nThese doctors specialize in %s:" % diagnosis )
for name, specialties in Doctors.items():
	if diagnosis in specialties:
		print( "Dr. " + name )
print( )
