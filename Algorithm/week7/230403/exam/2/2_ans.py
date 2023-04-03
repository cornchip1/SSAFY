import sys
sys.stdin = open('algo2_sample_in.txt','r')

def dfs(n,sm,cur):
    global ans

    if ans <= sm : return

    if n == N :
        if v[A] < v[B]:
            ans = min(ans,sm+arr[cur][0])
        return

    for j in range(1,N):
        if v[j] == 0 :
            v[j] = n
            dfs(n+1,sm+arr[cur][j],j)
            v[j] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    A,B = map(int,input().split())

    v = [0] * N
    ans = 100 * N + 1

    dfs(1,0,0)

    print(f'#{tc} {ans}')