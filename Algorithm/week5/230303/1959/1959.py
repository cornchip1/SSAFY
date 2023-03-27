import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    diff = N-M if N > M else M-N

    d = 0
    mx = -1*10**9

    while d <= diff:
        sm = 0
        if N > M :
            for j in range(M):
                sm += (A[j+d]*B[j])
        else:
            for i in range(N):
                sm += (A[i]*B[i+d])
        if sm > mx : mx = sm
        d += 1
    print(f'#{test_case} {mx}')