nl=[]
for i in range(9):
    n=int(input())
    nl.append(n)

print(max(nl))
print(nl.index(max(nl))+1)
