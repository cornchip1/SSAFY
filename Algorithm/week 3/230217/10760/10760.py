import sys
sys.stdin = open('input2.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split()) # arr의 크기 NxM
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0 # 후보지 개수

    for i in range(N):
        for j in range(M):
            cnt = 0 # 사진을 찍을 수 있는 구역의 개수
            # 상/하/좌/우/좌상단/좌하단/우상단/우하단 을 확인하여
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)):
                ni,nj = i+di, j+dj
                # 좌표값이 범위 내애 있다면
                if 0 <= ni < N and 0 <= nj < M :
                    # 그리고 착륙할 지점보다 높이가 낮다면 개수에 추가
                    if arr[i][j] > arr[ni][nj] : cnt += 1
            # 사진을 찍을 수 있는 구역이 4개 이상이면 후보지 개수에 추가
            if cnt >= 4 : ans += 1

    print(f'#{test_case} {ans}')