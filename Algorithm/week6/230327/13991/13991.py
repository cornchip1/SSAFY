import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # NxN array
    arr = [list(map(int,input().split())) for _ in range(N)]

    sm = 10*13+1
    # 오른쪽이나 아래로만 이동할 수 있다
    for i in range(N):
        

    print(f'#{test_case}')