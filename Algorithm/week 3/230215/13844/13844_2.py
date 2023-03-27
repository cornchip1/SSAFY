import sys
sys.stdin = open('s_input.txt','r')

def DFS(si,sj,ei,ej):
    # v,stk initialize
    v = [[0]*N for _ in range(N)]
    stk = []

    ci,cj = si,sj
    v[ci][cj] = 1

    while True :
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1 :
                stk.append((ci,cj))
                v[ni][nj] = 1
                ci,cj = ni,nj
                break
        else :
            if stk : ci,cj = stk.pop()
            else : break

    ans = v[ei][ej]
    return ans

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(int(_) for _ in input()) for _ in range(N)]

    si,sj,ei,ej = 0,0,0,0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2 : si,sj = i,j ; break
            if arr[i][j] == 3: ei, ej = i, j; break

    print(f'#{test_case} {DFS(si,sj,ei,ej)}')


