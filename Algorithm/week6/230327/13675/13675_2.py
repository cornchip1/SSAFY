import sys
sys.stdin = open('s_input.txt','r')

def dfs(n,cnt,sm):
    global ans

    if n == 12 :
        if cnt == N and sm == K:
            ans += 1
        return

    dfs(n+1,cnt+1,sm+A[n])
    dfs(n+1,cnt,sm)

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    A = [ _ for _ in range(1,13)]

    v = [0]*12
    ans = 0
    dfs(0,0,0)

    print(f'#{tc} {ans}')