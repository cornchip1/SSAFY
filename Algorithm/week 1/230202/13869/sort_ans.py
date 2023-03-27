import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input().split()))

    cnts = [0]*101
    for n in lst :
        cnts[n] += 1

    for i in range(1,len(cnts)) :
        cnts[i] += cnts[i-1]

    alst = [0]*N
    for n in lst :
        cnts[n] -= 1
        alst[cnts[n]] = n

    print(f'#{test_case} ',*alst)