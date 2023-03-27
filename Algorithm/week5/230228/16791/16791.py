import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]

    # 각 행별로 색별 칸 수 세기
    C = [] # W,B,R 순서
    for i in range(N):
        W,B,R = 0,0,0
        for j in range(M):
            if arr[i][j] == 'W' : W += 1
            elif arr[i][j] == 'B' : B += 1
            elif arr[i][j] == 'R' : R +=1
        C.append((W,B,R))

    # 바꿔야 하는 칸의 개수 초기화 : 첫줄과 마지막 줄은 무조건 W, R 로만 이루어져 있어야 함
    cnt = M-(C[0][1]+C[0][2])+M-(C[-1][0]+C[-1][1])

    # 나머지 줄에서 바꿔야 하는 칸의 개수
    lst = []
    for x in C[1:N-1]:
        print(x)

    print(f'#{test_case}')