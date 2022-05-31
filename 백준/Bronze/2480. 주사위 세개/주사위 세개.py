a,b,c=map(int, input().split())
r=0
if a==b and b==c:
    r=r+10000+a*1000
elif (a==b and b!=c) or (b==c and c!=a) or (c==a and a!=b):
    if a==b:
        r=r+1000+a*100
    elif b==c:
        r=r+1000+b*100
    else:
        r=r+1000+c*100
else:
    r=max(a,b,c)*100
    
print(r)