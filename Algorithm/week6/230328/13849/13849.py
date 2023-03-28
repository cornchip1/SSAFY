import sys
sys.stdin = open('s_input.txt','r')

# DFS, Backtracking
def dfs(n,sm):
    global ans

    # [3] 가지치기는 나중에
    if ans <= sm : return

    # [1] 종료 조건 : n 이 N 보다 크거나 같아지면 재귀 함수 호출을 종료한다
    if n >= N :
        ans = min(ans,sm)
        return

    # [2] 하부 함수 호출
    for j in range(N):
        if v[j] == 0 :
            v[j] = 1
            dfs(n+1,sm+arr[n][j])
            v[j] = 0 # 미방문 처리를 해줘야 선행 단계로 돌아올 수 있음

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    v = [0]*N
    ans = N*10 + 1
    dfs(0,0)

    print(f'#{tc} {ans}')