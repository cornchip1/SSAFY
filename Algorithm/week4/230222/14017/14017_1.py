import sys
sys.stdin = open('input.txt','r')

def preord(n) :
    if n:
        alst.append(n)
        preord(ch1[n])
        preord(ch2[n])


T = int(input())
for test_case in range(1,T+1):
    V = int(input())
    lst = list(map(int,input().split()))
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    for i in range(0,len(lst),2):
        p,c = lst[i],lst[i+1]
        if ch1[p] == 0 : ch1[p] = c
        else: ch2[p] = c

    alst = []
    preord(1)
    print(f'#{test_case}',*alst)