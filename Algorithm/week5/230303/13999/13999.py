import sys
sys.stdin = open('s_in1.txt','r')

lst=[[(-1,0),(1,0),(0,-1),(0,1)],[(-1,-1),(-1,1),(1,-1),(1,1)]]

T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split()) # NxN 배열, 각 방향으로 M칸
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    for si in range(N):
        for sj in range(N):
            for t in range(2):
                sm = arr[si][sj]
                for di,dj in lst[t]:
                    for m in range(1,M):
                        ni,nj = si+di*m,sj+dj*m
                        if 0 <= ni < N and 0 <= nj < N :
                            sm += arr[ni][nj]
                if sm > ans : ans = sm

    print(f'#{test_case} {ans}')