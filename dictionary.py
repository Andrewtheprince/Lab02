class Dictionary:
    def __init__(self, dict, dizionario={}):
        infile = open(dict, "r", encoding="utf-8")
        riga = infile.readline()
        while len(riga) != 0:
            pezzi = riga.strip().split(" ")
            traduzioni = []
            traduzioni.append(pezzi[1])
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

        pass