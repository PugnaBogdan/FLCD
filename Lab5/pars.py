import grammar as g
import sys
#sys.setrecursionlimit(5000)


class Parser:
    def __init__(self, grammar):

        self.grammar = grammar
        self.firstSet = {i: [] for i in self.grammar.N}
        self.followSet = {i: set() for i in self.grammar.N}
        self.table = {}
        #input stack
        self.alpha = list()
        #working stack
        self.beta = list()
        #output stack
        self.pi = list()

    def getFirst(self):

        return self.firstSet

    def generateFirstSet(self):
        for nonTerminal in self.grammar.N:
            self.firstSet[nonTerminal] = self.FirstOf(nonTerminal)


    def FirstOf(self, nonTerminal):

        temp = []
        for prod in self.grammar.getProductionForNonTerminal(nonTerminal):
            for time in prod:
                firstSymbol = time[0][0]
                # r = time.split()
                # firstSymbol = r[0]

                if firstSymbol == 'e':
                    temp.append("e")
                    break
                elif firstSymbol in self.grammar.T:
                    temp.append(firstSymbol)
                    break
                else:
                    l = self.FirstOf(firstSymbol)
                    return l
        return temp

    def checkNonTermianl(self, symbol):
        if symbol in self.grammar.N:
            return True
        return False

    def getProdsWithNonTerm(self, nonTerm):
        result = {}
        # print(nonTerm)
        for k,v in self.grammar.S.items():
            for item in v:

                if (nonTerm in item[0]):
                    result[k] = item[0]
                    #print(result.items())

        return result


    def follow(self):
        # init the follow for the starting symbol
        self.followSet[self.grammar.N[0]] = set("e")
        # for each non term we look in the productions that contain the non term in the rhs
        # print(self.grammar.N)

        for nonTerm in self.grammar.N:
            # print(nonTerm)
            for k, v in self.getProdsWithNonTerm(nonTerm).items():
                # print(v)
                for characterIndex in range(0, len(v)):
                    if (v[characterIndex][0] == nonTerm):
                        # print("char index eq non term")
                        if (characterIndex == len(v) - 1):
                            # print("case when it's the last")
                            # print(self.followSet[nonTerm])
                            # print(self.followSet[k])
                            # print(v)
                            self.followSet[nonTerm] = self.followSet[nonTerm].union(self.followSet[k])
                        else:
                            # print("case when there is somethign after it")
                            # print(self.followSet)
                            # print(self.followSet[nonTerm])
                            #print(v)
                            #print(v[characterIndex + 1])
                            if(v[characterIndex+1][0] in self.grammar.T):
                                self.followSet[nonTerm] = self.followSet[nonTerm].union(set(v[characterIndex+1][0]))
                            else:
                                # print(self.firstSet[k])
                                if("e" in set(self.firstSet[v[characterIndex + 1][0]])):
                                    self.followSet[nonTerm] = self.followSet[nonTerm].union(set(self.firstSet[v[characterIndex + 1][0]]).union(self.followSet[k]))
                                else:
                                    self.followSet[nonTerm] = self.followSet[nonTerm].union(
                                        set(self.firstSet[v[characterIndex + 1][0]]))
    def getFollow(self):
        return self.followSet

    def Table(self):

        for key, value in self.grammar.S.items():
            rowSymbol = key
            # print(key)
            # print(value)
            for v in value:
                production = v[0]
                #print(production)
                for columnSymbol in self.grammar.T + ['$']:
                    pair = (rowSymbol, columnSymbol)

                    if production[0] == columnSymbol and columnSymbol != 'e':
                        self.table[pair] = v
                    elif production[0] in self.grammar.N and columnSymbol in self.firstSet.get(production[0]):
                        if pair not in self.table:

                            self.table[pair] = v
                    else:
                        if production[0] == 'e':
                            #element is b
                            for element in self.followSet.get(rowSymbol):
                                if(element == 'e'):
                                    element = '$'
                                self.table[(rowSymbol,element)] = v


        for t in self.grammar.T:
            self.table[(t, t)] = ('pop')
        self.table[('$', '$')] = ('acc')

    #create the initial configuration
    def prepareStax(self,sequence):
        self.alpha = list()
        self.beta = list()
        self.pi = list()

        #put S$ in beta
        self.beta.append('$')
        self.beta.append(self.grammar.N[0])


        #put everything from the fronteer and $ in alpha
        self.alpha.append('$')
        for i in range(0, len(sequence)):
            self.alpha.append(sequence[len(sequence)-i-1])



        #add epsilon to pi
        self.pi.append('e')

    def parse(self,sequence):

        #create initial configuration like in the course
        self.prepareStax(sequence)
        print(self.alpha)
        print()
        print(self.beta)
        print()
        print(self.pi)
        print()
        go = True
        r = ""
        s = ""
        #algortimul din cursu 7
        while go:
            lastIndexAlpha = len(self.alpha) - 1
            lastIndexBeta = len(self.beta) - 1
            tableValue = self.table.get((self.beta[lastIndexBeta],self.alpha[lastIndexAlpha]))
            #print(tableValue)
            if (isinstance(tableValue, tuple) and tableValue!= None):
                #print(tableValue)
                self.beta.pop()
                if 'e' not in tableValue[0]:
                    for element in reversed(tableValue[0]):
                        self.beta.append(element)
                self.pi.append(tableValue[1])
                r = r+"\n"+self.grammar.getProdutionForIndex(tableValue[1])
            elif (tableValue == "pop"):
                self.beta.pop()
                self.alpha.pop()
            elif(tableValue == "acc"):
                go = False
                s = "acc"
            else:
                s = "err"
                go = False

        if s == "acc":
            print("Sequence accepted")

            out1 = open('D:\\anul3\\semestrul1\\FLCD\\Lab5\\out1.txt', 'w')  # pugna
            out1.write(str(self.pi))
            out1.write(r)
            return self.pi
        else:
            print("Sequence not accepted")


