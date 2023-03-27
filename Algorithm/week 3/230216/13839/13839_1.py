import sys
sys.stdin = open('s_input.txt','r')

def dfs(n, sm):
    global ans
    # 종료 조건: 원소의 합(sm) == K
    if n == N:  # 전체 경우의 수를 따져서 모든 부분집합을 만들어봤을 때
        if sm == K: ans += 1  # 종료 조건을 만족하면 ans 에 1을 더한다
        return

    dfs(n + 1, sm + lst[n])  # 부분집합이 lst의 n번째 원소를 포함하는 경우
    dfs(n + 1, sm)  # 부분집합이 lst의 n번째 원소를 포함하지 않는 경우


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # N: 집합의 길이 K: 원소의 합
    lst = list(map(int, input().split()))  # 주어진 리스트
    ans = 0  # 정답 초기화, 해당하는 부분집합이 없을 경우 0을 출력
    dfs(0, 0)
    print(f'#{test_case} {ans}')