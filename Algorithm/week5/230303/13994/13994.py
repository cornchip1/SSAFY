import sys
sys.stdin = open('sample_in.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    L = [0]*1001
    for _ in range(N):
        t, S, E = map(int,input().split())
        if t == 1 :
            for l in range(S,E+1): L[l] += 1
        elif t == 2:
            L[S] += 1
            L[E] += 1
            if S % 2 :
                for l in range(S+1,E):
                    if l % 2 : L[l] += 1
            else:
                for l in range(S+1,E):
                    if l % 2 == 0 : L[l] += 1
        elif t == 3 :
            L[S] += 1
            L[E] += 1
            if S % 2 :
                for l in range(S+1,E) :
                    if l % 3 == 0 and l % 10 : L[l] += 1
            else:
                for l in range(S+1,E):
                    if l % 4 == 0 : L[l] += 1

    print(f'#{test_case} {max(L)}')