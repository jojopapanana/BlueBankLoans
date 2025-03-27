#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 11:22:29 2025

@author: jovannamelissa
"""

import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

json_data = open('loan_data_json.json')
loans = json.load(json_data)

#transform to data frame

loan_data = pd.DataFrame(loans)

loan_data['purpose'].unique()
loan_data.describe()
loan_data['fico'].describe()
loan_data['dti'].describe()

#using np's exponent function to calculate annual income
loan_data['log.annual.inc'] = np.exp(loan_data['log.annual.inc'])

ficocat = []
for i in loan_data['fico']:
    
    try:
        if i >= 300 and i < 400:
            cat = 'Very Poor'
        elif i >= 400 and i < 600:
            cat = 'Poor'
        elif i >= 601 and i < 660:
            cat = 'Fair'
        elif i >= 661 and i < 700:
            cat = 'Good'
        elif i >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
        
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)
loan_data['fico.category'] = ficocat

#df.loc as conditional statements

loan_data.loc[loan_data['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loan_data.loc[loan_data['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'


#number of loans by fico category

catplot = loan_data.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()


#scatterplot

ypoint = loan_data['log.annual.inc']
xpoint = loan_data['dti']
plt.scatter(xpoint, ypoint, color = 'yellow')
plt.show()


loan_data.to_csv('loan_cleaned_new_version.csv', index = True)














