import sys
sys.stdin = open('input.txt','r')

def dfs(i,sm):
    global ans

    if i == N :
        if sm > ans :
            ans = sm
        return

    for j in range(N):
        if v[j] == 0 :
            v[j] = 1
            tmp = sm*arr[i][j]
            if tmp > ans :
                dfs(i+1,sm*arr[i][j])
            v[j] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    v = [0]*N
    dfs(0,1)
    ans = round(ans/10**6,6)

    print(f'#{tc} {ans:.6f}')

