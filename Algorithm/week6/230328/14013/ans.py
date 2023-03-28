import sys
sys.stdin = open('s_input.txt','r')

def dfs_1(n,sm,v):
    global ans
    if ans <= sm : return
    if n == N :
        ans = min(ans,sm)
        return

    for j in range(N):
        if j not in v : # 미방문인 경우
            dfs_1(n+1,sm+arr[n][j],v+[j])

def dfs_2(n,sm):
    global ans
    if ans <= sm:
        return
    if n == N:
        ans = min(ans,sm)
        return
    for j in range(N):
        if j not in v : # 미방문인 경우
            v.append(j)
            dfs_2(n+1,sm+arr[n][j])
            v.pop()

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = N*99 + 1

    # [1] 비어있는 v 배열을 parameter로 전달
    #dfs_1(0,0,[])
    # [2] 빈 배열을 만들어 append & pop 진행
    v = []
    dfs_2(0,0)

    print(f'#{tc} {ans}')