import sys
sys.stdin = open('s_input.txt','r')

def dfs(n,sm) :
    global ans
    # 가지치기는 제일 위, 최솟값을 구하는 문제 == 가지치기 해라
    if ans <= sm : return # 더이상 진행해도 정답 갱신 가능성이 없을 때 가지치기를 한다

    # 종료 조건 먼저 설정
    if n == N :
        if ans > sm : ans = sm
        return

    # n+1 하부함수 호출 - j 를 사용했는지 확인하기 위한 장치
    for j in range(N):
        # # 3. 함수 내에서 확인하는 방법
        # if j not in stk :
        #     dfs(n+1,sm+arr[n][j],v+[j])
        #
        # # 2. stk 을 이용해서 j를 확인
        # if j not in v :
        #     stk.append(j)
        #     dfs(n+1,sm+arr[n][j])
        #     stk.pop()

        # 1. visited 배열을 사용하는 방법
        if v[j] == 0 : # 또는 if not v[j] :
            v[j] = 1
            dfs(n+1,sm+arr[n][j])
            v[j] = 0 # 사용 후 반드시 리셋 필요

T = int(input())
for test_case in range(1,T+1) :
    N = int(input()) # NxN 배열
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = 10*N

    v = [0]*N # 1 이 방법이 가장 빠름
    dfs(0, 0)

    # stk = [] # 2 # 3
    # dfs(0,0,[]) # 3

    print(f'#{test_case} {ans}')