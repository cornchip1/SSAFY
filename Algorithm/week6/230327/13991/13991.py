import sys
sys.stdin = open('s_input.txt','r')

def dfs(i,j,sm):
    global ans

    # [1] 종료 조건
    if i == j == N - 1:
        if sm < ans : ans = sm
        return

    # [2] 하부 호출
    if i == N-1 :
        dfs(i, j + 1, sm + arr[i][j + 1])  # 오른쪽으로 가는 경우
    elif j == N-1:
        dfs(i + 1, j, sm + arr[i + 1][j])  # 아래로 가는 경우
    else:
        dfs(i+1,j,sm+arr[i+1][j]) # 아래로 가는 경우
        dfs(i, j + 1, sm + arr[i][j + 1])  # 오른쪽으로 가는 경우

T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # NxN array
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = 10*13+1
    
    dfs(0,0,arr[0][0])
    

    print(f'#{test_case} {ans}')