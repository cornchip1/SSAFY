import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1

    for i in range(1,N):
        for j in range(N):
            arr[i][j] = arr[i-1][j-1]+arr[i-1][j]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 : arr[i][j] = ''

    print(f'#{test_case}')

    for i in range(N):
        print(*arr[i])