import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Read dataset
df = pd.read_csv(r'F:\IMDb_project5\dataset\imdb_movies_2024(2) - imdb_movies_2024(2).csv.csv')

# Display first five rows
print(df.head())

# Display column names
print(df.columns)

# Dataset shape
print(df.shape)

# Information
print(df.info())

# Missing values
print(df.isnull().sum())

# Duplicate values
print(df.duplicated().sum())

df['Movie_Title'] = df['Movie_Title'].str.replace(
    r'^\d+\.\s*', '', regex=True)

def cleaned_text(text):
  text=text.lower()
  text=re.sub(r'[^a-zA-Z0-9\s]','',text)
  text=re.sub(r'\s+',' ',text)
  return text.strip()
df['cleaned_storyline'] = df['Storyline'].apply(cleaned_text)

#Remove duplicate cleaned storylines
print(df['cleaned_storyline'].duplicated().sum())
df_new = df.drop_duplicates(subset=["cleaned_storyline"]).copy()


print("Total rows:", len(df_new))

print("Unique storylines:", df_new['Storyline'].nunique())

print("Unique movie names:", df_new['Movie_Title'].nunique())

df_new['combine_text']=df_new['Movie_Title']+' '+df_new['cleaned_storyline']

 #Save cleaned dataset
df_new.to_csv("cleaned_movies.csv", index=False)
print("Data cleaning completed!")
