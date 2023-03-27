import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(_ for _ in input()) for _ in range(N)]
    ans = 'NO'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o' :
                si,sj = i,j;
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
                    cnt = 0
                    for k in range(5):
                        ni,nj = si + di*k, sj + dj*k
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                            cnt += 1
                    if cnt >= 5 : ans = 'YES' ; break
    print(f'#{test_case} {ans}')