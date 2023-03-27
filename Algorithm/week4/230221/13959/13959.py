import sys
sys.stdin = open('s_input.txt','r')

def BFS(si,sj,ei,ej) :
    # 2 q, v[] 생성
    q = []
    v = [[0]*N for _ in range(N)]

    # 3 q에 초기데이터(들) 삽입 후 v 표시
    q.append((si,sj))
    v[si][sj] = 1 # 방문 표시 / += 1 로 해도 됨

    while q : # q가 비어있지 않을 때
        ci,cj = q.pop(0) # 첫번째 원소를 가져온다
        # 정답 처리는 이곳에서 / ci == ei, cj == ej 이면 종료지점까지 무사히 온 것
        if (ci,cj) == (ei,ej) : return v[ei][ej]-2 # 출발, 도착 칸은 이동 거리에서 제외한다

        # 4 네 개 방향 반복 처리
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            # 범위 내, 미방문, 조건에 맞으면 (즉, 벽(1) 이 아니면)
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj]+1 # 이동 거리를 저장 (현재 위치까지 얼마나 걸렸는지 저장됨)

    else: return 0 # q가 빌 때까지 탐색했지만 return 을 하지 못한 경우 길이 없다


T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # NxN 배열
    arr = [list(int(i) for i in input()) for _ in range(N)] # 미로

    # 1 si,sj,ei,ej 저장
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2 : si,sj = i,j ; break
            if arr[i][j] == 3 : ei,ej = i,j ; break

    print(f'#{test_case} {BFS(si,sj,ei,ej)}')