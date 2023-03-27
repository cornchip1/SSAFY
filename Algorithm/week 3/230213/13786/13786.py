#파스칼의 삼각형
import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input()) #크기가 N인 파스칼의 삼각형을 출력하라
    arr = [[] for _ in range(N)]

    for i in range(N):
        for j in range(i + 1):
            arr[i].append(1)
            if 2 <= i < N and 1 <= j < i:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

    print(f'#{test_case}')
    for i in range(N):
        print(*arr[i])


