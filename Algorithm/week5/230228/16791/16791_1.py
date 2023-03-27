import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(_ for _ in input()) for _ in range(N)]
    ans = 0

    for i in range(0,N-2):
        for j in range(i+1,N-1):
            cnt = 0
            for s in range(0,i+1):
                cnt += arr[s].count('W')
            for s in range(i+1,j+1):
                cnt += arr[s].count('B')
            for s in range(j+1,N):
                cnt += arr[s].count('R')

            ans = max(ans,cnt)

    print(f'#{test_case} {N*M-ans}')
