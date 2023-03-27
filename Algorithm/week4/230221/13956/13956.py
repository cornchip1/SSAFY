import sys
sys.stdin = open('s_input.txt','r')

def BFS(si,sj):
    # 필요한 변수들 생성
    q = []
    ci,cj = si,sj
    q.append([ci,cj])
    arr[ci][cj] = 1

    # 단위 작업
    while q:
        ci,cj = q.pop(0)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 :
                q.append([ni,nj])
                arr[ni][nj] = 1

T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # NxN 배열
    arr = [list(int(i) for i in input()) for _ in range(N)] # 미로

    # 출발 좌표, 도착 좌표 찾기 - 출발점 : 2, 도착점 : 3
    si,sj,ei,ej = 0,0,0,0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2 :
                si,sj = i,j
                break
            elif arr[i][j] == 3 :
                ei,ej = i,j
                break

    BFS(si,sj)
    ans = arr[ei][ej]
    if arr[ei][ej] == 3 : ans = 0

    print(f'#{test_case} {ans}')