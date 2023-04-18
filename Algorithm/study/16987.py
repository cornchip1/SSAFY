def eggcnt(egg):
    cnt = 0
    for e in egg:
        if e[0] <= 0: cnt += 1
    return cnt

def dfs(n):
    global ans

    if n >= N :
        ans = max(ans,eggcnt(egg))
        return

    if egg[n][0] > 0 : # 계란이 안깨졌으면
        allbroken = True
        for i in range(N): # 계란 중에서

            if i != n and egg[i][0] > 0 : # 지금 손에 든 계란이 아닌 계란을 치고, 그 안 깨진 계란이면
                allbroken = False
                egg[i][0] -= egg[n][1] # 계란 내구도 빼기
                egg[n][0] -= egg[i][1]
                dfs(n+1) # 다음 계란으로 건너뛴다
                egg[i][0] += egg[n][1] # 계란 내구도 복구
                egg[n][0] += egg[i][1]
        if allbroken == True : dfs(N)


    else : dfs(n+1) # 계란이 깨졌으면 한 칸 오른쪽 계란으로 다시 시도


N = int(input())
egg = []
ans = 0
for _ in range(N):
    hp, w = map(int,input().split())
    egg.append([hp,w])

v = [0]*N
dfs(0)

print(ans)