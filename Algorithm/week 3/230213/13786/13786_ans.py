#파스칼의 삼각형
import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input()) #크기가 N인 파스칼의 삼각형을 출력하라
    arr = [[1]*_ for _ in range(1,N+1)]

    for i in range(2,N):
        for j in range(1,i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print(f'#{test_case}')
    for lst in arr :
        print(*lst)