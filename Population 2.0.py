import requests 
from spellchecker import SpellChecker
spell=SpellChecker()
from thefunctions import *
import pandas as pd
# todo Make functions for getting
# Making a dictionary for 2020
url = 'https://www.worldometers.info/world-population/population-by-country/'
html = requests.get(url).content
df_list = pd.read_html(html)
df=df_list[0]
countries2020 = list()
populations2020=list()

for country in df.loc[0:235, "Country (or dependency)"]:
    countries2020.append(country)


for population in df.loc[0:235, "Population (2020)"]:
    populations2020.append(population)

# Making a dictionary for 2000

url2 = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_in_2000'
html2 = requests.get(url2).content
df_list2 = pd.read_html(html2)
df2=df_list2[2]


countries2000 = list()
populations2000 = list()
for country in df2.loc[0:235, "Country/Territory"]:
    country = str(country)
    if "(" in country:
        first = country.find("(")
        country=country[:first-1]
        countries2000.append(country)
    else:
        countries2000.append(country)

for population in df2.loc[0:235, "Population2000estimate"]:
    if "[" in population:
        first = population.find("[")
        population=population[:first-1]
        populations2000.append(population)
    else:
        populations2000.append(population)
dictonary2000 = dict(zip(countries2000,populations2000))
dictonary2020 = dict(zip(countries2020,populations2020))

while True:
    UserInput=input("Enter a year (2000 or 2020): ")
    UserInput = int(UserInput)
    if UserInput == 2000:
        x= dictonary2000
        break
    if UserInput == 2020:
        x = dictonary2020
        break
    else: 
        print('Invalid input')

GetPopulations(x)

