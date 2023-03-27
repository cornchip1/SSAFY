import sys
sys.stdin = open('s_input.txt','r')

def dfs(n,sm) :
    global ans # 재귀에서 ans 외에는 절대 global로 쓰지 않는다

    # 가지치기는 제일 위에서
    # 그런데 오히려 시간이 더 오래 걸릴 수 있으므로 최솟값을 찾을 때 등등 몇몇 경우에만 쓴다
    # if sm > K :
    #     return
    # 시작은 무조건 종료 조건 설정부터
    if n == N :
        if sm == K : ans += 1
        return
    # 하부 함수 호출 : 포함/미포함
    dfs(n+1,sm + lst[n]) # 1 포함하는 경우
    dfs(n+1,sm) # 2 포함하지 않는 경우


T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())
    lst = list(map(int,input().split()))
    ans = 0

    dfs(0,0)

    print(f'#{test_case} {ans}')