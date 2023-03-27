import sys
sys.stdin = open('input.txt','r')

def BFS(si,sj,ei,ej):
    # 1 필요한 것들 생성
    global ans
    q = []
    v = [[0]*N for _ in range(N)]

    # 2 초기 작업
    q.append((si,sj))
    v[si][sj] = 1

    # 3
    while q :
        ci,cj = q.pop(0) # 3-1 q 에서 첫번째 원소를 가져온다
        # 4 정답 처리: 도착 지점에 도달할 수 있다면
        if (ci,cj) == (ei,ej) :
            ans = 1
        # 3-2 상/하/좌/우 이동 & 미방문 & 조건(벽(1) 이 아님) 부합 시
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1 :
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1

T = 10
for test_case in range(1,T+1):
    _ = input()
    N = 100
    arr = [list(int(i) for i in input()) for _ in range(N)]
    ans = 0 # 도달 가능하면 1

    # 출발점, 도착점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2 : si,sj = i,j ; break
            if arr[i][j] == 3 : ei,ej = i,j ; break

    BFS(si,sj,ei,ej)
    print(f'#{test_case} {ans}')
