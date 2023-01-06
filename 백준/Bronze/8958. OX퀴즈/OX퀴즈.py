n=int(input())

for _ in range(n):
    ox=list(input())
    score=0
    s_score=0
    for o in ox:
        if o=="O":
            score+=1
            s_score+=score
        else:
            score=0

    print(s_score)