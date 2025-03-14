import dictionary as di

class Translator:

    def __init__(self):
        self.d = None

    def printMenu(self):
        print("--------------------------------")
        print("Translator Alien-Italian")
        print("--------------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit")

    def loadDictionary(self, dict):
        self.d = di.Dictionary(dict)

    def handleAdd(self, entry):
        self.d.addWord(entry)

    def handleTranslate(self, query):
        self.d.translate(query)

    def handleWildCard(self,query):
        self.d.translateWordWildCard(query)
