import dictionary as di

class Translator:

    def __init__(self):
        pass

    def printMenu(self):
        print("--------------------------------")
        print("Translator Alien-Italian")
        print("--------------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit")

    def loadDictionary(self, dict):
        d = di.Dictionary(dict)

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parolaAliena = entry[0]

        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass