class Dictionary:
    def __init__(self, dict):
        dizionario = {}
        infile = open(dict, "r", encoding="utf-8")
        riga = infile.readline()
        while len(riga) != 0:
            pezzi = riga.strip().split(" ")
            traduzioni = []
            traduzioni.append(pezzi[1])
            dizionario[pezzi[0]]=traduzioni
            riga = infile.readline()

    def addWord(self, entry):
        pass

    def translate(self):
        pass

    def translateWordWildCard(self):
        pass