import sys
sys.stdin = open('input.txt','r')

T = 10
for test_case in range(1,T+1):
    _ = input()
    N = 100
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 시작점, 출발점 찾기
    si,sj = 99,0
    for j in range(N):
        if arr[si][j] == 2 : sj = j

    # 거꾸로 타고 올라가기
    ci, cj = si, sj

    while ci > 0 :
        for di,dj in ((0,-1),(0,1),(-1,0)):
            ni,nj = ci+di,cj+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 :
                arr[ni][nj] = 2 # 방문처리
                ci,cj = ni,nj

    ans = 0
    for ej in range(N):
        if arr[0][ej] == 2: ans = ej

    print(f'#{test_case} {ans}')