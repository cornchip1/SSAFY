import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # 미로의 크기 (NxN)

    # 출발지에서 목적지까지 도착하는 경로가 존재하는가
    # 0: 통로 1: 벽 2: 출발 3: 도착

    arr = [list(int(_i) for _i in input()) for _ in range(N)] # 미로 받기

    si, sj, ei, ej = 0,0,0,0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2: # 시작점
                si,sj = i,j
            if arr[i][j] == 3 : # 도착점
                ei,ej = i,j

    # 상/하/좌/우
    di = [-1,+1,0,0]
    dj = [0,0,-1,+1]

    istk, jstk = [],[]
    v = [[0]*N for _ in range(N)]
    v[si][sj] = 1

    while [si,sj] != [ei,ej] :
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0 <= ni < N and 0 <= nj < N :
                if v[ni][nj] == 0 :
                    if arr[ni][nj] != 1 : #  미방문 & 연결됨
                        istk.append(si)
                        jstk.append(sj)
                        si,sj = ni,nj
                        v[si][sj] = 1
                        break
                else : # 방문함, 연결 안됨
                    if istk != [] and jstk != [] : si,sj = istk.pop(),jstk.pop()
                    else :
                        break

    if [si,sj] == [ei,ej] :
        ans = 1

    print(f'#{test_case} {ans}')
