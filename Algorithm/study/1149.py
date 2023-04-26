N = int(input())
dp = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,N):
    # 빨간집 : 0
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    # 초록집 : 1
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    # 파란집 : 2
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

print(min(dp[N-1]))
