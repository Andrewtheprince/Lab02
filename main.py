import translator as tr

t = tr.Translator()


while True:

    t.printMenu()
    t.loadDictionary("dictionary.txt")
    txtIn = input()

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        txtIn = input()
        controllo = False
        pezzi = txtIn.split(" ")
        while not controllo:
            for s in pezzi:
                if s.isalpha():
                    controllo = True
                    s.lower()
                else:
                    print("Non sono ammessi caratteri diversi da lettere")
                    txtIn = input()
        entry =(pezzi[0], pezzi[1])
        t.handleAdd(entry)

    elif int(txtIn) == 2:
        print("Ok, quale parola devo tradurre?")
        txtIn=input()
        controllo = False
        while not controllo:
            if txtIn.isalpha():
                controllo = True
                txtIn.lower()
            else:
                print("Non sono ammessi caratteri diversi da lettere")
                txtIn = input()
        t.handleTranslate(txtIn)

    elif int(txtIn) == 3:
        pass
    
    elif int(txtIn) == 4:
        break