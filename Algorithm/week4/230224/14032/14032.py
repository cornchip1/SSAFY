import sys
sys.stdin = open('s_input.txt','r')

def COUNT(i,j):
    global lst

    si,sj = ci,cj = i,j
    cnt = 1
    while True:
        check = 0
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            if 0 <= ni < N and 0 <= nj < N :
                if arr[ci][cj] +1 == arr[ni][nj] :
                    check += 1
                    cnt += 1
                    ci, cj = ni, nj
        if check == 0 : lst[arr[si][sj]] = cnt ; break
        else: continue

    return

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    lst = [0] * (N**2+1)

    for i in range(N):
        for j in range(N):
            COUNT(i,j)

    mx,mxidx = 0,0
    for idx,v in enumerate(lst) :
        if v > mx : mxidx,mx = idx,v

    print(f'#{test_case} {mxidx} {mx}')