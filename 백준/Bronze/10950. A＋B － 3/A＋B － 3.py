num=int(input())
l1 = list()
l2 = list()
for i in range(num):
    a,b=map(int, input().split())
    l1.append(a)
    l2.append(b)
    
for j in range(num):
    print((l1[j]+l2[j]))