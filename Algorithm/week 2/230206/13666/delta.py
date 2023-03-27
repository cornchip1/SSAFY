import sys
sys.stdin = open('s_list2_연습문제1_iin.txt','r')

T = int(input())
for test_case in range(1,T+1) :
    N = int(input())
    arr = [list(map(int,input().split())) for n in range(N)]

    di = [+1, -1, 0, 0] #아래로, 위로
    dj = [0, 0, +1, -1] #오른쪽으로, 왼쪽으로

    s = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ri = i + di[k]
                rj = j + dj[k]
                if 0 <= ri < N and 0 <= rj < N :
                    result = arr[i][j] - arr[ri][rj] if arr[i][j] - arr[ri][rj] >0 else -(arr[i][j] - arr[ri][rj])
                    s += result

    print(f'#{test_case} {s}')