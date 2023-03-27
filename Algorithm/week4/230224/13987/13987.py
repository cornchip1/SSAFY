# 2117
import sys
sys.stdin = open('sample_input.txt','r')

T = 1 #int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    K = K1 = 3
    k = K
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 :
                arr[i][j] = 2

                s = 1

                while s <= K1 :
                    for hi, hj in ((0,0),(0, -1), (0, 1)):  # horizontally
                        nhi,nhj = i + hi*s,j+hj*s

                        k = K
                        while k >= 1:
                            for vi, vj in ((0,0),(-1, 0), (1, 0)):  # vertically
                                ni, nj = nhi + vi * k, nhj + vj * k
                                if 0 <= ni < N and 0 <= nj < N:
                                    arr[ni][nj] = 2
                            k -= 1
                    s += 1
                    K -= 1



    print(arr)
    print(f'#{test_case}')