from Tables import SymbolTable as st

size = 3

myl = ['1', '2', '3', '4']

ST = st.STT(size)

for x in myl:
    ST.add(x)

print(ST.get_st_pos('4'))
print(ST)


print(ST.get_st_pos('6'))
print(ST)

