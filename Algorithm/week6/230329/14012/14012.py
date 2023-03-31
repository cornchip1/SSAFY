import sys
sys.stdin = open('s_input.txt','r')

def dfs(n,cnt,b):
    global ans

    if ans <= cnt : return
    if n == N-1 :
        ans = min(ans,cnt)
        return

    if b > 0 :
        dfs(n + 1, cnt, b - 1)
    dfs(n+1, cnt+1, lst[n]-1)



T = int(input())
for tc in range(1,T+1):
    _ = list(map(int,input().split()))
    N, lst = _[0],_[1:]

    ans = N+1
    v = [0]*N
    dfs(1,0,lst[0]-1)

    print(f'#{tc} {ans}')