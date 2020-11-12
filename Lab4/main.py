import FA as f


class main:

    finiteAutomata = f.FA()

    def readFile(self):

        self.finiteAutomata.getInput()

    def printFA(self):
        if self.finiteAutomata.getOK():
            print(self.finiteAutomata)
        else:
            print("read file first")

    def checkSequence(self):
        seq = input("type sequence here: ")
        print(self.finiteAutomata.checkSequence(seq))

    def menu(self):
        print("1 - read input")
        print("2 - print fa")
        print("3 - check sequence")

    def run(self):
        menuChoices = {'1': self.readFile,
                '2': self.printFA,
                '3': self.checkSequence}
        exit = False
        while True:
            self.menu()
            choice = input("-")
            if choice in menuChoices.keys():
                menuChoices[choice]()
            else:
                break

x = main()

x.run()