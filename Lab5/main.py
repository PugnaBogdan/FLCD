import null as null

import grammar as g
from pars import Parser

class UI:


    def __init__(self):
        self.grammar = g.Grammar()
        self.parser = None

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
            print(str(self.grammar.getProductionForNonTerminal(noTerminal)))
        else:
            print("read file first")

    def printFirstSet(self):
        self.parser = Parser(self.grammar)
        self.parser.generateFirstSet()
        print(self.parser.getFirst())

    def menu(self):
        print("1 - read input")
        print("2 - print Productions")
        print("3 - print NonTerminals")
        print("4 - print Terminals")
        print("5 - print Production for terminal")
        print("6 - print FirstSet")


    def run(self):
        menuChoices = {'1': self.readFile,
                       '2': self.printGrammar,
                       '3': self.printNonTerminals,
                       '4': self.printTerminals,
                       '5': self.printProduction,
                       '6': self.printFirstSet
                       }
        while True:
            self.menu()
            choice = input("-")
            if choice in menuChoices.keys():
                menuChoices[choice]()
            else:
                break


ui = UI()

ui.run()