cnt=0
n=int(input())
orgn=n

while True:
    n1=n//10
    n2=n%10
    n3=(n1+n2)%10
    n=(n2*10)+n3
    cnt+=1
    if n==orgn:
        break

print(cnt)