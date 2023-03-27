import sys
sys.stdin = open('s_input.txt','r')

def DFS(si,sj):
    stk = []

    ci,cj = si,sj
    arr[ci][cj] = '1' # 재방문 방지를 위해 이동한 위치를 벽으로 처리

    while True :
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N  and arr[ni][nj] != '1' :
                stk.append([ci,cj])
                ci,cj = ni,nj
                arr[ci][cj] = '1'
                break
        else :
            if stk: ci,cj = stk.pop()
            else : break

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 1 출발 좌표, 도착 좌표 찾기
    si,sj,ei,ej = 0,0,0,0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2' :
                si,sj = i,j
                break
            elif arr[i][j] == '3' :
                ei,ej = i,j
                break

    # 3 정답 처리
    DFS(si,sj)
    ans = arr[ei][ej]
    if ans == '3' : ans = '0'

    print(f'#{test_case} {ans}')