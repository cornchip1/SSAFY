n,k = map(int,input().split())
coins = [ int(input()) for _ in range(n)]

dp = [0] * (k+1)

# dp list 채우기
for i in range(k+1):
    if dp[i] == 0 : # 값이 채워져있지 않다면
        if 0 < i < min(coins) : dp[i] = -1 # 만들 수 없음
        elif i in coins : dp[i] = 1 # 동전 한개로 만들 수 있음

        lst = []
        for c in coins :
            # 동전을 하나 뺐을 때 그 합이 음수가 아니고, 만들 수 없는 값이 아니면
            if i - c >= 0 and dp[i-c] > -1 :
                lst.append(dp[i-c])
        if lst : dp[i] = min(lst) + 1 # 하나 이상의 묶음이 있다면 그중 최솟값, 동전 하나 더하기
        else: # 음수이거나 만들 수 없는 값이었으면 이 값도 만들 수 없음 (단, 0보다 클 경우 제외)
            if i > 0 : dp[i] = -1

print(dp[k])