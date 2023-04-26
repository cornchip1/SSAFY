N = int(input()) # 남은 일수, N+1 일에 퇴사
labour = [list(map(int,input().split())) for _ in range(N)]

dp = [0]*(N+1)

for i in range(N): # i번째 날에 일을 한다면
    for j in range(i+labour[i][0], N+1): # 일에 소요되는 시간 이후의 날에
        if dp[j] < dp[i] + labour[i][1]: # 소득이 i 번째 날의 소득보다 작다면
            dp[j] = dp[i] + labour[i][1] # i 번째 날에 일을 한 소득을 dp[j] 에 넣는다

print(dp[N])