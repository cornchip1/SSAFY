import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    plane = [[0]*10 for _ in range(10)]
    cnt = 0
    for _ in range(N):
        r1,c1,r2,c2,colour = map(int,input().split())
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                plane[r][c] += colour

    for i in range(10):
        for j in range(10):
            if plane[i][j] == 3 :
                cnt += 1

    print(f'#{test_case} {cnt}')

