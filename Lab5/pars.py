import grammar as g


class Parser:
    def __init__(self, grammar):

        self.grammar = grammar
        self.firstSet = {i: [] for i in self.grammar.N}
        self.followSet = {i: set() for i in self.grammar.N}
        self.table = {}

    def getFirst(self):

        return self.firstSet

    def generateFirstSet(self):
        for nonTerminal in self.grammar.N:
            self.firstSet[nonTerminal] = self.FirstOf(nonTerminal)


    def FirstOf(self, nonTerminal):

        temp = []
        terminals = self.grammar.T
        for prod in self.grammar.getProductionForNonTerminal(nonTerminal):
            for time in prod:
                firstSymbol = time[0]

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
        print(nonTerm)
        for k,v in self.grammar.S.items():
            for item in v:

                if (nonTerm in item):
                    result[k] = item
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
                    if (v[characterIndex] == nonTerm):
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
                            print(v)
                            #print(v[characterIndex + 1])
                            if(v[characterIndex+1] in self.grammar.T):
                                self.followSet[nonTerm] = self.followSet[nonTerm].union(set(v[characterIndex+1]))
                            else:
                                print(self.firstSet[k])
                                if("e" in set(self.firstSet[v[characterIndex + 1]])):
                                    self.followSet[nonTerm] = self.followSet[nonTerm].union(set(self.firstSet[v[characterIndex + 1]]).union(self.followSet[k]))
                                else:
                                    self.followSet[nonTerm] = self.followSet[nonTerm].union(
                                        set(self.firstSet[v[characterIndex + 1]]))
    def getFollow(self):
        return self.followSet
#     if (firstSet.containsKey(nonTerminal))
#         return firstSet.get(nonTerminal);
#     Set<String> temp = new HashSet<>();
#     Set<String> terminals = grammar.getTerminals();
#     for (Production production : grammar.getProductionsForNonterminal(nonTerminal))
#         for (List<String> rule : production.getRules()) {
#             String firstSymbol = rule.get(0);
#             if (firstSymbol.equals("ε"))
#                 temp.add("ε");
#             else if (terminals.contains(firstSymbol))
#                 temp.add(firstSymbol);
#             else
#                 temp.addAll(firstOf(firstSymbol));
#         }
#     return temp;
# }

