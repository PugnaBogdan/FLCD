
class Grammar:

    def __init__(self):
        self.__N = []
        self.__T = []
        self.__S = {}
        self.__OK = False


    def getOK(self):
        return self.__OK

    def readFile(self):

        finiteFile = open('D:\\anul3\\semestrul1\\FLCD\Lab5\\g1', 'r')
        lines = finiteFile.readlines()
        count = 0
        for line in lines:
            if count == 0:
                self.__N = line.strip(' ').split()
                count += 1
                continue
            if count == 1:
                self.__T = line.strip(' ').split()
                count += 1
                continue
            if count>1:

                resultDest =[]
                linesProds = line.strip(' ').split("->")
                NonTerminal = linesProds[0][0]
                listDest = linesProds[1].strip().split(' | ')
                for destination in listDest:
                    resultDest.append(destination)
                self.__S[NonTerminal] = resultDest
                count+=1

        self.__OK = True

    def printTerminals(self):
        rT = "T = {"
        for x in range(0, len(self.__T)):
            rT = rT + str(self.__T[x])
            if (x == len(self.__T) - 1):
                rT = rT + "}\n"
            else:
                rT = rT + ", "
        return rT

    def printNonTerminals(self):
        rN = "N = {"
        for x in range(0, len(self.__N)):
            rN = rN + str(self.__N[x])
            if (x == len(self.__N) - 1):
                rN = rN + "}\n"
            else:
                rN = rN + ", "
        return rN

    def printProduction(self, nonTerminal):
        res = ""

        for x in range(0, len(self.__S[nonTerminal])):
            res = res + self.__S[nonTerminal][x]
            if (x == len(self.__S[nonTerminal])-1):
                res = res + "\n"
            else:
                res = res + ", "

        return res

    def __str__(self):

        return str(self.__S)



