def GetPopulations(dictionary):
    "Allows you to output populations of countries listed in the variable dictionarry"
    while True:
        from spellchecker import SpellChecker
        spell=SpellChecker()
        UserInput=input("Name a country: ")
        if UserInput=="done":
            break
        if UserInput == "list":
            print(*dictionary)
            continue
        if UserInput in dictionary:
            print(dictionary[UserInput])
        else:
            # todo Remove redundant lists
            words= UserInput.split()
            countryWords = list()
            for word in words:
                countryWords.append(word)
            fullName =str()
            for word in countryWords:
                option=spell.correction(word)
                option=option.capitalize()
                fullName=fullName+option+' '
            fullName=fullName.rstrip()
            
            if fullName not in dictionary:
                print(f"There\' no country called '{UserInput}' ")
                continue
            answer =input(f'Did you mean \"{fullName}\"? ')
            answer=answer.lower()
            if answer == 'yes':
                try:
                    print(dictionary[fullName])
                except:
                    print(f'The country called {fullName} cannot be found')
                    continue
# Defining get index 
def GetTableIndex(url):
    html = rs.get(url).content
    df_list = pd.read_html(html)
    a = -1
    for table in df_list:
        a +=1
        for header in table:
            for row in table.loc[:,header]:
                if row == "Ukraine":
                    b=a
    return(b)
# Get name colomn
def GetPopColomn(url):
    html = rs.get(url).content
    df_list = pd.read_html(html)
    b = "loser"
    for table in df_list:
        if b == "sex":
            break
        for header in table:
            print(header)
            if b == "sex":
                c = header
                break
            for row in table.loc[:,header]:
                if row == "Ukraine":
                    b = "sex"
    return(c)

def GetNameColomn(url):
        html = rs.get(url).content
        df_list = pd.read_html(html)
        d = "loser"
        for table in df_list:
            for header in table:
                for row in table.loc[:,header]:
                    if row == "Ukraine":
                        d = header
                        break
                    
        return(d)
# Defining creeating dictionary for countries:
def GetDict(url):
    names = list()
    populations = list()
    import pandas as pd
    import requests as rs
    html = rs.get(url).content
    df_list = pd.read_html(html)    
    df=df_list[GetTableIndex(url)]
    for name in df.loc[:,GetNameColomn(url)]:
        if "(" in name:
            first = name.find("(")
            name=name[:first-1]
            names.append(name)
        else: names.append(name)
    for population in df.loc[:,GetPopColomn(url)]:
        populations.append(population)
    countries = dict(zip(names,populations))
    return countries

