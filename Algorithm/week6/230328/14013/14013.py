import sys
sys.stdin = open('s_input.txt','r')

def dfs(n,sm):
    global ans

    if ans <= sm : return
    if n >= N :
        ans = min(ans,sm)
        return
    else:
        for j in range(N):
            if v[j] == 0 :
                v[j] = 1
                dfs(n+1,sm+arr[n][j])
                v[j] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    v = [0]*N
    ans = 100 * N
    dfs(0,0)

    print(f'#{tc} {ans}')