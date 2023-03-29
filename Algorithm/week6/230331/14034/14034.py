import sys
sys.stdin = open('input.txt','r')

def dfs(h,sm):
    global ans
    if h >= N :
        if sm >= B :
            ans = min(ans,sm)
    else:
        v[h] = 0
        dfs(h+1,sm+H[h])
        v[h] = 1
        dfs(h+1,sm)


T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    H = list(map(int,input().split()))

    v = [0]*N
    sm = 0
    ans = 10000*20+1
    dfs(0,sm)

    print(f'#{tc} {ans-B}')
