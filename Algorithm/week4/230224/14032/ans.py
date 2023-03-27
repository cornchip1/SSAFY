import sys
sys.stdin = open('s_input.txt','r')

def bfs(si,sj):
    # 0 필요한 변수들 생성
    q = []
    alst = []

    # 1 초기 작업
    q.append((si,sj))
    v[si][sj] = 1
    alst.append(arr[si][sj])

    while q:
        ci,cj = q.pop(0) # 2 q에서 꺼내기

        # 4방향/미방문/조건: 나랑 1 차이가 나면
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and abs(arr[ci][cj]-arr[ni][nj]) == 1:
                q.append((ni,nj))
                v[ni][nj] = 1
                alst.append(arr[ni][nj])

    return min(alst),len(alst)


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    ans,cnt = N*N,0

    for si in range(N):
        for sj in range(N):
            if v[si][sj] == 0 :
                t,tcnt = bfs(si,sj) # 정답 갱신
                if cnt < tcnt or cnt == tcnt and ans > t :
                    ans, cnt = t,tcnt

    print(f'#{test_case} {ans} {cnt}')