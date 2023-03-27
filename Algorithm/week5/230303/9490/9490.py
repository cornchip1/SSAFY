import sys
sys.stdin = open('input1.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(M):
            sm = arr[i][j]
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                for a in range(1,arr[i][j]+1):
                    ni,nj = i+di*a,j+dj*a
                    if 0 <= ni < N and 0 <= nj < M :
                        sm += arr[ni][nj]
            if sm > ans : ans = sm

    print(f'#{test_case} {ans}')