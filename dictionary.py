class Dictionary:
    def __init__(self, dict, dizionario={}):
        infile = open(dict, "r", encoding="utf-8")
        riga = infile.readline()
        while len(riga) != 0:
            pezzi = riga.strip().split(" ")
            traduzioni = [pezzi[1]]
            dizionario[pezzi[0]]=traduzioni
            riga = infile.readline()
        infile.close()
        self.dizionario = dizionario

    def addWord(self, entry):
        controllo = False
        for chiave, valore in self.dizionario.items():
            if chiave == entry[0]:
                valore.extend(entry[1])
                controllo = True
                print(chiave,valore)
                print("Aggiunta!")
                break
        if not controllo:
            self.dizionario[entry[0]] = entry[1]
            print(entry)
            print("Aggiunta!")


    def translate(self, query, risultato=""):
        controllo = False
        for chiave, valore in self.dizionario.items():
            if chiave == query:
                for s in valore:
                    risultato += s
                    risultato += " "
                print(risultato)
                controllo = True
        if not controllo:
            print("La parola non è presente nel dizionario")

    def translateWordWildCard(self, query):
        pezzi = query.split("?")
        control = False
        for chiave, valore in self.dizionario.items():
            if (pezzi[0] in chiave) and (pezzi[1] in chiave ) and (len(chiave) == len(query)):
                contatore = 0
                for s in chiave:
                    if s not in query:
                        contatore += 1
                if contatore <= 1:
                    print(chiave)
                    print(valore)
                    control = True
        if not control:
            print("La parola non è presente nel dizionario")