# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:08:44 2024

@author: zizip
"""

import pandas as pd

df = pd.read_csv("movie_dataset.csv")
df.columns = df.columns.str.strip().str.replace(' ', '_')

df['Metascore'].fillna(df['Metascore'].mean(), inplace=True)
df['Revenue_(Millions)'].fillna(df['Revenue_(Millions)'].mean(), inplace=True)

df.dropna(inplace=True)

print(df.head())

print(df['Rating'].max())

max_index = df['Rating'].idxmax()

maximum_rated = df.loc[max_index]

print("max_rated:", maximum_rated)

avg = df['Revenue_(Millions)'].mean()

print("Average Revenue:", avg)

filtered_file = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

avg_with_range= filtered_file['Revenue_(Millions)'].mean()

print(avg_with_range) 

movies = df[df['Year'] == 2016]

num = len(movies)

print("Number of Movies:", num)

director_name= df[df['Director'] == "Christopher Nolan"]

num = len(director_name)

print("Movies by Christopher Nolan:", num)

ratings = df[df['Rating'] >= 8.0]

rating= len(ratings)
print("Movies with a raring of atleast 8.0: ",rating )

director_nolan= df[df['Director'] == "Christopher Nolan"]

median_rating= director_nolan['Rating'].median()

print("Median rating for Christopher Nolan:", median_rating)

avg_by_year = df.groupby('Year')['Rating'].mean()

highest_rating = avg_by_year.idxmax()

highest_avg_rating = avg_by_year.max()
print(f"The year is {highest_rating} with the average rating of {highest_avg_rating:.2f}.")

filtered_file = df[(df['Year'] >= 2005) & (df['Year'] <= 2016)]

m_2006 = len(filtered_file[filtered_file['Year'] == 2006])
m_2016 = len(filtered_file[filtered_file['Year'] == 2016])

percentage = ((m_2016 - m_2006) / m_2006) * 100

print(f"The percentage increase is {percentage:.2f}%.")

actors = df['Actors'].str.split(', ').explode()

common_actor = actors.value_counts().idxmax()

print(f"The most common actor is '{common_actor}' ")

genre = df['Genre'].str.split(', ').explode()
num_g = genre.nunique()
print("unique genre:",num_g)

num_df = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = num_df.corr()

print("Correlation Matrix:", correlation_matrix)



