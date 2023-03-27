import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    si,sj = 0,0
    cnt = 1
    arr[si][sj] = 1

    while cnt < N*N :
        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            for n in range(N):
                ni,nj = si+di,sj+dj
                if 0 <= ni < N and 0 <= nj < N :
                    if arr[ni][nj] != 0 : pass
                    else:
                        cnt += 1
                        arr[ni][nj] = cnt
                        si,sj = ni,nj



    print(f'#{test_case}')
    for i in range(N):
        print(*arr[i])
