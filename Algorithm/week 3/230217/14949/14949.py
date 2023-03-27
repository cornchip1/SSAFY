import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(input().split()) for _ in range(N)]
    ans = 0 # 가장 큰 구조물의 길이 (0 으로 initialise)

    # 배열을 돌며 구조물을 찾는다
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1' :

                # 아래 방향, 오른쪽 방향으로 탐색
                for di, dj in ((1, 0), (0, 1)):
                    cnt = 0
                    for n, m in zip(range(N), range(M)):
                        ni,nj = i + di*n , j + dj*m
                        if 0 <= ni < N and 0 <= nj < M :
                            if arr[ni][nj] == '1' :
                                cnt += 1
                            if arr[ni][nj] == '0' : break
                    if cnt > ans : ans = cnt

    print(f'#{test_case} {ans}')
