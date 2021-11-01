import requests
import pandas as pd

url = 'https://www.worldometers.info/world-population/population-by-country/'
html = requests.get(url).content
df_list = pd.read_html(html)
df=df_list[-1]

countries2020 = list()
for country in df.loc[0:235, "Country (or dependency)"]:
    countries2020.append(country)


populations2020=list()
for population in df.loc[0:235, "Population (2020)"]:
    populations2020.append(population)

dictonary = dict(zip(countries2020,populations2020))


url2 = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_in_2000'
html2 = requests.get(url2).content
df_list2 = pd.read_html(html2)
df2=df_list2[2]
# print(df2)

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
print(dictonary2000)



    


