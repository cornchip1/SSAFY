import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1) :
    N = int(input()) # NxN 행렬
    arr = [ input().split() for _ in range(N)]

    # no.  # 0          # 90            # 180           # 270
    # 1    # 00 01 02   # 20 10 00      # 22 21 20      # 02 12 22
    # 2    # 10 11 12   # 21 11 01      # 12 11 10      # 01 11 21
    # 3    # 20 21 22   # 22 12 02      # 02 01 00      # 00 10 20

    cnt = 0

    # 0
    for i in range(N) :
        for j in range(N) :
            arr[i][j]

    # 90
    for i in range(N-1,-1,-1) :
        for j in range(N):
            print(arr[i])

    # 180
    for i in range(N):
        for j in range(N):
            print(arr[j][i])