import sys
sys.stdin = open('sample_input (3).txt','r')

def cal(tlst1,tlst2):
    # 같은 재료값인 경우 0이므로, 모든 조합 : 누적
    sm1,sm2 = 0,0
    for i in range(M):
        for j in range(M):
            sm1 += arr[tlst1[i]][tlst1[j]]
            sm2 += arr[tlst2[i]][tlst2[j]]
    return abs(sm1-sm2)

def dfs(n,tlst1,tlst2):
    global ans

    if n == N :
        if len(tlst1) == M:
            ans = min(ans,cal(tlst1,tlst2))
        return

    dfs(n+1,tlst1+[n],tlst2) # A에 재료 n 을 선택
    dfs(n+1,tlst1,tlst2+[n]) # B에 재료 n 을 선택


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    M = N//2
    ans = 20000*N*N +1
    dfs(0,[],[])

    print(f'#{tc} {ans}')