import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    cnts = [0]*100
    temp = [0] * N

    for i in lst :
        cnts[i] += 1

    for j in range(N-1,-1,-1) :
        if cnts[lst[j]] >= 1 :
            temp[j] = lst[j]
            cnts[lst[j]] -= 1

    print(temp)