
import Tables.ProgramInternalFile as p
import Tables.SymbolTable
pif = p.PIF()
class Scanner:

    reservedWords = []
    separators = []
    operators = []
    constantCode = ""
    identifierCode = ""

    def TokenizeTokenFile(self):
        TokenFile = open('D:/anul3/semestrul1/FLCD/Scanner/InputFiles/token.in','r')
        Lines = TokenFile.readlines()
        count = 0
        for line in Lines:
            count+=1
            if count<=10:
                self.operators.append(line.strip())
            elif count>10 and count <=22:
                self.reservedWords.append(line.strip())
            elif count>22 and count<=34:
                self.separators.append(line.strip())
            elif count == 35:
                self.identifierCode = line.strip()
            else:
                self.constantCode = line.strip()
        self.separators.append(" ")


    def detect(self):
        pass

    def scann(self):
        problemFile = open('D:/anul3/semestrul1/FLCD/Scanner/InputFiles/pb1.txt','r')
        Lines = problemFile.readlines()
        count = 0
        for line in Lines:
            for word in line.split():
                #print(word)
                if word.strip() in self.operators or word.strip() in self.reservedWords:
                    pif.add(word,0)
                    continue
                i=0
                myW = ""

                for i in range(len(word)):

                    myW= myW+word[i]
                    if i == len(word)-1:
                        if myW in self.operators or myW in self.reservedWords:
                            pif.add(myW, 0)
                            continue
                        pif.add(myW,1)
                        myW=""
                        continue
                    if word[i + 1] in self.separators:
                        if myW in self.operators or myW in self.reservedWords:
                            pif.add(myW, 0)
                            myW=""
                            continue
                        else:
                            pif.add(myW, 1)
                            myW=""
                            continue
                            #constant or identifier
                    if word[i] in self.separators:
                        pif.add(word[i],0)
                        myW = ""











x = Scanner()

x.TokenizeTokenFile()
x.scann()

print(pif)