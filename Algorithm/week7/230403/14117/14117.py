import sys
sys.stdin = open('input.txt','r')

def bfs(si,sj,ei,ej):
    inf = 100**16

    ci,cj = si,sj
    v = [[inf] * N for _ in range(N)]
    q = [(ci,cj)]
    v[ci][cj] = arr[ci][cj]

    while q:
        (ci,cj) = q.pop(0)

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[ci][cj] + arr[ni][nj] :
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]

    return v[ei][ej]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list( int(_i) for _i in input()) for _ in range(N)]

    ans = bfs(0,0,N-1,N-1)

    print(f'#{tc} {ans}')