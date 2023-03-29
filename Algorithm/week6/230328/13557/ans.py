import sys
sys.stdin = open('s_input.txt', 'r')

def check(lst):
    cnt = 0
    # [0:3] or [3:6] 값이 run, triplet
    for i in range(0,N,3): # 0부터 N까지 3씩 건너뛰면서 // 가변적일 수 있기 때문에 일반화
        if lst[i] == lst[i+1] == lst[i+2] or lst[i] + 2 == lst[i+1]+1 == lst[i+2] :
            cnt += 1
    return cnt == 2

def dfs(n,tlst):
    global ans
    # [1] 종료 조건
    if n >= N :
        if check(tlst):
            ans = 1
        return

    # [2] 하부 함수 호출
    for j in range(N): # lst를 돌면서
        if v[j] == 0 : # j 번째 원소가 미방문이면
            v[j] = 1
            dfs(n+1,tlst+[lst[j]])
            v[j] = 0

T = int(input())
for tc in range(1,T+1):
    lst = list(map(int,input()))

    N = 6
    v = [0] * N
    ans = 0
    dfs(0,[])

    print(f'#{tc} {ans}')