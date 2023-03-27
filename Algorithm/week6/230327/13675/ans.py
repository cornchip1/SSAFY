import sys
sys.stdin = open('s_input.txt','r')

# 백트래킹 문제 

def dfs(n,cnt,sm):
    global ans 
    
    # [0] 가지치기는 가장 위에서, 순서로는 가장 마지막에 하기
    # cnt > CNT 인 경우 정답이 될 가능성이 없음 
    # 또는 sm > K 인 경우 정답이 될 가능성이 없음
    if cnt > CNT or sm > K : return 
    

    # [1] 종료조건 (n에 관련) // 정답처리는 이곳에서
    if n == N :
        if cnt == CNT and sm == K : ans += 1 
        return
    
    # [2] 하부 호출
    dfs(n+1, cnt+1, sm + lst[n]) # 사용하는 경우
    dfs(n+1, cnt, sm) # 사용하지 않는 경우

T = int(input())
for test_case in range(1,T+1):
    CNT, K = map(int,input().split())
    N = 12
    lst = [n for n in range(1,N+1)]

    # main loop 에서는 dfs의 가장 위 노드를 호출
    # n, cnt, sm
    ans = 0
    dfs(0,0,0)
    
    print(f'#{test_case} {ans}')