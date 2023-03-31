import sys
sys.stdin = open('s_input.txt','r')

def dfs (i,n,sm):
    global ans

    if i == A :
        if n == N and sm == K:
            ans += 1
        return

    dfs(i+1,n+1,sm+lst[i])
    dfs(i+1,n,sm)


T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    A = 12
    lst = [ _ for _ in range(1,A+1)]
    ans = 0
    v = [0]*A

    dfs(0,0,0)

    print(f'#{tc} {ans}')