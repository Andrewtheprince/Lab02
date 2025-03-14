import re

import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")

while True:

    t.printMenu()
    txtIn = input()

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        txtIn = input()
        control = False
        pezzi = txtIn.split(" ")
        while not control:
            for s in pezzi:
                if s.isalpha():
                    control = True
                    s.lower()
                else:
                    print("Non sono ammessi caratteri diversi da lettere")
                    txtIn = input()
        traduzioni = []
        traduzioni.extend(pezzi)
        traduzioni.pop(0)
        entry =(pezzi[0], traduzioni)
        t.handleAdd(entry)

    elif int(txtIn) == 2:
        print("Ok, quale parola devo tradurre?")
        txtIn=input()
        control = False
        while not control:
            if txtIn.isalpha():
                control = True
                txtIn.lower()
            else:
                print("Non sono ammessi caratteri diversi da lettere")
                txtIn = input()
        t.handleTranslate(txtIn)

    elif int(txtIn) == 3:
        print("Ok, quale parola devo cercare?")
        txtIn = input()
        control = False
        while not control:
            if re.fullmatch(r'[a-zA-Z?]+', txtIn):
                t.handleWildCard(txtIn.lower())
                control = True
            else:
                print("La parola inserita può contenere solo lettere e '?'")
                txtIn = input()

    elif int(txtIn) == 4:
        break
