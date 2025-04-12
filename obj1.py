import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/V/Desktop/COVID-19.csv")

df = df.drop_duplicates()

numeric_cols = ['Cases - Weekly', 'Deaths - Weekly', 'Tests - Weekly', 'Case Rate - Weekly']
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

df['ZIP Code'] = df['ZIP Code'].astype(str) 
df['Week Start'] = pd.to_datetime(df['Week Start']) 
df['Week End'] = pd.to_datetime(df['Week End'])
for col in numeric_cols:
    df[col] = df[col].astype(float) 

df.to_csv('C:/Users/V/Desktop/cleaned_covid_data.csv', index=False)

print("Data cleaning completed. Summary:")
print(df.info())
print(df.head())
