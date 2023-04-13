from collections import deque

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr = [[0]*M for _ in range(N)]

    # 1. 배추 저장
    lst = []
    for _ in range(K):
        s,e = map(int,input().split())
        arr[s][e] = 1
        lst.append((s,e))

    # 2. 배추 리스트 돌기
    # 2-1. 배추벌레 세는 함수 만들기
    cnt = 0 # 초기화
    def bfs(si,sj):
        global cnt
        q = deque()
        q.append((si,sj))

        while q:
            e = 0  # 주변 배추의 개수
            ci,cj = q.popleft()
            arr[ci][cj] = 2

            # 배추 상/하/좌/우 탐색
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni,nj = ci+di,cj+dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 :
                    arr[ni][nj] = 2 # 방문처리
                    e += 1 # 인근 배추의 개수 1 증가
                    q.append((ni,nj)) # 다음 배추로 이동

        # 종료 조건: 인근에 배추가 더 이상 없을 때 == q가 비어있을 때
        cnt += 1
        return

    for l in lst:
        si,sj = l[0],l[1]
        if arr[si][sj] == 1 : bfs(si,sj)

    print(f'{cnt}')
