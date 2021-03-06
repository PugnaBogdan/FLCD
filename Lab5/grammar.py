
class Grammar:

    def __init__(self):
        self.N = []
        self.T = []
        self.S = {}
        self.__OK = False


    def getOK(self):
        return self.__OK

    def readFile(self):

        #finiteFile = open('C:\\Users\\Rares2\\Desktop\\an3\\sem1Eu\\FLCD\\pguna\\FLCD\\Lab5\\g1') # rares
        finiteFile = open('D:\\anul3\\semestrul1\\FLCD\\Lab5\\g1', 'r') # pugna
        lines = finiteFile.readlines()
        count = 0
        index  = 0
        for line in lines:
            if count == 0:
                self.N = line.strip(' ').split()
                count += 1
                continue
            if count == 1:
                self.T = line.strip(' ').split()
                count += 1
                continue
            if count>1:

                resultDest =[]
                linesProds = line.split("->")
                NonTerminal = linesProds[0].strip(' ')
                listDest = linesProds[1].strip().split(' | ')
                for destination in listDest:
                    index+= 1
                    resultDest.append((destination,index))
                self.S[NonTerminal] = resultDest
                count+=1

        self.__OK = True

    def printTerminals(self):
        rT = "T = {"
        for x in range(0, len(self.T)):
            rT = rT + str(self.T[x])
            if (x == len(self.T) - 1):
                rT = rT + "}\n"
            else:
                rT = rT + ", "
        return rT

    def printNonTerminals(self):
        rN = "N = {"
        for x in range(0, len(self.N)):
            rN = rN + str(self.N[x])
            if (x == len(self.N) - 1):
                rN = rN + "}\n"
            else:
                rN = rN + ", "
        return rN

    def getProductionForNonTerminal(self, nonTerminal):
        res = []

        for x in range(0, len(self.S[nonTerminal])):
            res.append(self.S[nonTerminal][x])

        return res

    def getProdutionForIndex(self, index):
        r = ""
        for item in self.S:
            for item2 in self.S[item]:
                if item2[1] == index:
                    r = r+str(item)+" -> "+str(item2[0])

        return r

    def __str__(self):
        return str(self.S)



