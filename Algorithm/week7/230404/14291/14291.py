import sys
sys.stdin = open('sample_in.txt','r')

# 10개 중 4개만 맞음

def bfs(si,sj,ei,ej):
    inf = 100*100*1000
    v = [[inf]*N for _ in range(N)]
    q = [(si,sj)]
    v[si][sj] = 0

    while q :
        ci,cj= q.pop(0)

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            if 0 <= ni < N and 0 <= nj < N:
                diff = 0
                if arr[ni][nj] > arr[ci][cj]:
                    diff = arr[ni][nj] - arr[ci][cj]

                if v[ni][nj] > v[ci][cj] + diff + 1 :
                    q.append((ni,nj))
                    v[ni][nj] = v[ci][cj] + diff + 1

    return v[ei][ej]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = bfs(0,0,N-1,N-1)

    print(f'#{tc} {ans}')