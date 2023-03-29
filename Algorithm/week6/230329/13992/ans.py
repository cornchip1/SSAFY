import sys
sys.stdin = open('s_input.txt','r')

def dfs(n,sm,s):
    global ans

    if ans <= sm : return # 가지치기

    if n == N :
        sm += arr[s][0]
        ans = min(sm,ans)
        return

    for i in range(1,N):
        if v[i] == 0 :
            v[i] = 1
            dfs(n+1,sm+arr[s][i],i)
            v[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = 100*N+1
    v = [1]+[0]*(N-1)
    dfs(1,0,0) # n : 방문한 구역의 수 / sm : 전기 사용량 / s : 시작점

    print(f'#{tc} {ans}')