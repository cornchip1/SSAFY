N = int(input())
lst= list(map(int,input().split()))
dp = [0]*(N+1)

for i in range(N):
    for j in range(i):
        # 부분수열의 마지막 값보다 큰 값이라면
        if lst[i] > lst[j] and dp[i] < dp[j]: # dp[i] 보다 dp[j] 가 작으면 업데이트
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
