N = int(input())
scores = [0] * 301
for _ in range(N):
    scores[_] = int(input())
# dp list 생성 : 그 계단을 밟았을 때의 maximum 점수
dp = [0]*301

# 초기값 세팅 (1,2 차례로 밟거나 1,3 밟거나 2,3 밟거나 할 수 있음)
dp[0] = scores[0] # 첫번째 계단을 밟았을 때의 점수
dp[1] = scores[1]+scores[0] # 첫번째 계단과 두번째 계단을 밟았을 때의 점수
# 첫번재 계단과 세번째 계단을 밟거나, 두번째 계단과 세번째 계단을 밟은 값 중 큰 점수
dp[2] = max(scores[0]+scores[2], scores[1]+scores[2])

# 네번째 계단부터
for i in range(3,N):
    # 하나 뛰어 밟거나 연속으로 밟거나 할 수 있음 // 그 중 큰 값 저장하기
    dp[i] = max(dp[i-3]+ scores[i-1] + scores[i], dp[i-2]+scores[i])
print(dp[N-1])