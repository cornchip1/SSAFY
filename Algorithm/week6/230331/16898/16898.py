import sys
sys.stdin = open('sample_input.txt','r')

def dfs(n,N,sm):
    global ans
    if n >= N :
        if sm == K : ans += 1
        # print(*lst)
    else:
        v[n] = 0
        dfs(n + 1, N, sm + A[n])
        #dfs(n+1,N,lst + [A[n]])
        v[n] = 1
        dfs(n+1,N,sm)
        #dfs(n+1,N,lst)

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    A = list(map(int,input().split()))

    ans = 0
    v = [0]*N
    #lst = []
    #dfs(0,N,lst)
    dfs(0,N,0)

    print(f'#{tc} {ans}')