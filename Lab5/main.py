import grammar as g

class UI:
    grammar = g.Grammar()

    def readFile(self):

        self.grammar.readFile()

    def printGrammar(self):
        if self.grammar.getOK():
            print(self.grammar)
        else:
            print("read file first")

    def printNonTerminals(self):
        if self.grammar.getOK():
            print(self.grammar.printNonTerminals())
        else:
            print("read file first")

    def printTerminals(self):
        if self.grammar.getOK():
            print(self.grammar.printTerminals())
        else:
            print("read file first")

    def printProduction(self):
        noTerminal = input("type nonTerminal here: ")
        if self.grammar.getOK():
            print(self.grammar.printProduction(noTerminal))
        else:
            print("read file first")


    def menu(self):
        print("1 - read input")
        print("2 - print Productions")
        print("3 - print NonTerminals")
        print("4 - print Terminals")
        print("5 - print Production for terminal")


    def run(self):
        menuChoices = {'1': self.readFile,
                       '2': self.printGrammar,
                       '3': self.printNonTerminals,
                       '4': self.printTerminals,
                       '5': self.printProduction}
        exit = False
        while True:
            self.menu()
            choice = input("-")
            if choice in menuChoices.keys():
                menuChoices[choice]()
            else:
                break


ui = UI()

ui.run()