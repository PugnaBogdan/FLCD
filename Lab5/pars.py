import grammar as g

class Parser:
    def __init__(self, grammar):

        self.grammar = grammar
        self.firstSet = {i: [] for i in self.grammar.N}
        self.followSet = {i: [] for i in self.grammar.N}
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
                    temp.append(self.FirstOf(firstSymbol))
                    return temp
        return temp

    def checkNonTermianl(self, symbol):
        if symbol in self.grammar.N:
            return True
        return False

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