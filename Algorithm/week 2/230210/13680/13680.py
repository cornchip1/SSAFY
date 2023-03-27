import sys
sys.stdin = open('s_input.txt', 'r')



T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(int(i) for i in input().split()) for _ in range(N)]


    ans = 0
    for si in range(N):
        for sj in range(N):
            cnt = 0
            if arr[si][sj] == 1 :
                cnt += 1
                for di,dj in ((0,1),(1,0)):
                    ni,nj = si+di, sj+dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == 1 : cnt +=1
                        else : cnt = 0
            if cnt == K : ans += 1

    print(f'#{test_case} {ans}')
