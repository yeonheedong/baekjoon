def d(n):
    n=n+sum(map(int,str(n)))
    return n

s = set() # non-self number set / self number : 생성자가 없는 숫자

for i in range(1,10001):
    s.add(d(i))

for j in range(1,10001):
    if j not in s:
        print(j)