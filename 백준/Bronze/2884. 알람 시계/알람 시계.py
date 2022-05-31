h, m = map(int, input().split())

if m<45 and h>0:
    print(h-1, m+15) # m = m + 60 - 45
elif m>44:
    print(h,m-45)
else:
    print(23,m+15) # h==0, m<45일 때