import sys
sys.stdin = open('s_input.txt','r')

A = [_ for _ in range(1,13)]

def dfs(n,sm,cnt):
    global ans

    # 종료 조건: N개의 원소를 갖고 있고, 원소의 합이 K일 때
    if n == len(A) :
        if sm == K and cnt == N : ans += 1
        return
    dfs(n+1,sm+A[n],cnt+1) # 포함하는 경우
    dfs(n+1,sm,cnt) # 포함하지 않는 경우

T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split()) # A의 부분집합 중 N개의 원소를 갖고 있고, K : 원소의 합
    ans = 0

    dfs(0,0,0)

    print(f'#{test_case} {ans}')