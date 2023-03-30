import sys
sys.stdin = open('sample_input (3).txt','r')

def dfs(n,i,j):
    global cnt

    if n == N :
        cnt += 1
        return

    # 모든 경우의 수
    for j in range(N):
        if vi[i] == 0 :
            vi[i] = 1
            dfs(n+1,i+1,j)
            vi[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    vi,vj = [0]*N, [0]*N
    cnt = 0
    dfs(0,0,0)

    print(f'#{tc} {cnt}')
