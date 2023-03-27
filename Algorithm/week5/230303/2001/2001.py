import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
           sm = 0 #arr[i][j]
           for si in range(i,i+M):
               for sj in range(j,j+M):
                   if 0 <= si < N and 0 <= sj < N :
                       sm += arr[si][sj]
           if sm > ans : ans = sm

    print(f'#{test_case} {ans}')