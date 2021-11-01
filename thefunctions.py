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

