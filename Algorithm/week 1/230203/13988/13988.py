import sys
sys.stdin = open('s_bus2in.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # 노선의 수
    cnts = [0]*1000
    ans = 0
    for x in range(N):
        i, A, B = map(int,input().split())
        if i == 1 :
            for s in range(A,B+1) :
                cnts[s-1] += 1
        elif i == 2:
            for s in range(A,B+1) :
                if s == A or s == B:
                    cnts[s-1] += 1
            for s in range(A+1,B):
                if A % 2 :
                    if s % 2 :
                        cnts[s-1] += 1
                elif A % 2 == 0 :
                    if s % 2 == 0:
                        cnts[s-1] += 1
        elif i == 3:
            for s in range(A, B + 1):
                if s == A or s == B:
                    cnts[s - 1] += 1
            for s in range(A + 1, B):
                if A % 2:
                    if s % 3 == 0 and s % 10 != 0:
                        cnts[s - 1] += 1
                elif A % 2 == 0:
                    if s % 4 == 0:
                        cnts[s - 1] += 1
    for j in cnts :
        if j > ans :
            ans = j
        else :
            pass
    print(f'#{test_case} {ans}')