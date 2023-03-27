import sys
sys.stdin = open('input.txt','r')

def bfs(si,sj,ei,ej) :
    # 0 q, v 등 생성
    q = []
    v = [[0] * N for _ in range(N)]

    # 1 초기데이터 삽입, v 표시 : 단위작업
    q.append((si,sj))
    v[si][sj] = 1

    # 2 단위작업
    # 2-1 q가 비어있지 않다면
    while q:
        ci,cj = q.pop(0) # q의 첫번째 element 불러오기
        # 2-3 필요 시 정답 처리
        # 2-3-1 도착지점까지 갈 수 있는 경우
        if (ci,cj) == (ei,ej) : return 1

        # 2-2 반복 처리 - 상/하/좌/우 이동
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            # 범위 내, 미방문, 조건 부합 (벽이 아닐 때) 시
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1 :
                q.append((ni,nj))
                v[ni][nj] = 1 # 또는 v[ci][cj] + 1

    # 2-3-2 모두 탐색했으나 도착지점까지 갈 수 없는 경우
    return 0


T = 10
for test_case in range(1,T+1):
    _ = input()
    N = 16
    arr = [list(int(_) for _ in input()) for _ in range(N)]

    # 출발지, 목적지 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si,sj = i,j
            elif arr[i][j] == 3:
                ei,ej = i,j

    ans = bfs(si,sj,ei,ej)
    print(f'#{test_case} {ans}')