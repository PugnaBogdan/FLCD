from Tables import SymbolTable as st
from Tables import ProgramInternalFile as pif
import LexicalAnalizer.scanner as sc
import re as regex
# size = 3
#
# myl = ['1', '2', '3', '4']
#
# ST = st.STT(3)
#
# for x in myl:
#     ST.add(x)
#
# print(ST.get_st_pos('4'))
#
# x = ST.get_st_pos('6')
# x = ST.get_st_pos('12')
# print(x)
#
# print(ST)


s = st.STT(10)
p = pif.PIF()
fileName = 'D:/anul3/semestrul1/FLCD/Scanner/InputFiles/pb3err.txt'

scan = sc.Scanner(s, p, fileName)

scan.scann()

print(scan.get_st())
print(scan.get_pif())


