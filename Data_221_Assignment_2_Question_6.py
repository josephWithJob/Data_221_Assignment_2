# Assignment 2 Question 5
# Joseph Krosel

# Imports library
import pandas as pd
import numpy

# Reads the file and saves it
crime_information = pd.read_csv('crime.csv')

# Creates variables
violent_crime_category = []
pct_unemployment_high_crime = []
pct_unemployment_low_crime = []

# Sorts through the list to check for conditions and manipulates list
for index in range(0, len(crime_information)):
    if crime_information.iloc[index, 5] >= 0.50:
        violent_crime_category.append("HighCrime")
        pct_unemployment_high_crime.append(crime_information.iloc[index, 1])
    else:
        violent_crime_category.append("LowCrime")
        pct_unemployment_low_crime.append(crime_information.iloc[index, 1])

# Puts information into 'crime.csv'
crime_information['risk'] = violent_crime_category
crime_information.to_csv('crime.csv', index=False)

# Prints information
print(f"Average unemployment rate for high crime: {numpy.mean(pct_unemployment_high_crime)}. "
      f"Average unemployment rate for low crime: {numpy.mean(pct_unemployment_low_crime)}")