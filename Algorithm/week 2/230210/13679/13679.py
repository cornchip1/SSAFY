import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    mx = 0
    for i in range(N):
        for j in range(N):
            sm = 0
            for n in range(M):
                for m in range(M):
                    ni = i + n
                    nj = j + m
                    if 0 <= ni < N and 0 <= nj < N:
                        sm += arr[ni][nj]

            if sm > mx :
                mx = sm

    print(f'#{test_case} {mx}')