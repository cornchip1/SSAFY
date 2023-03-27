import sys
sys.stdin = open('s_input (1).txt','r')

di = [-1,+1,0,0,-1,+1,-1,+1] # 상/하/좌/우/좌상단/좌하단/우상단/우하단
dj = [0,0,-1,+1,-1,-1,+1,+1]

T = int(input())
for test_case in range(1,T+1) :
    N = int(input()) # NxN 판
    arr = [input() for _ in range(N)]
    ans = 'NO'

    for i in range(N) :
        for j in range(N) :
            if arr[i][j] == 'o' :
                for k in range(8) :
                    cnt = 0
                    for n in range(5):
                        ni,nj = i+di[k]*n,j+dj[k]*n
                        if 0 <= ni < N and 0 <= nj < N :
                            if arr[ni][nj] == 'o' :
                                cnt += 1
                        else : pass
                    if cnt == 5 : ans = 'YES'

    print(f'#{test_case} {ans}')

