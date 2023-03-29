import sys
sys.stdin = open('s_input.txt','r')

def dfs(n,cnt,b):
    global ans
    if ans <= cnt : return
    if n == N-1 :
        ans = min(ans,cnt)
        return
    else:
        # 교체하는 경우 : 항상 가능해서 체크할 필요 X
        dfs(n+1,cnt+1,lst[n]-1)
        # 교체하지 않는 경우 : 배터리 잔량 > 0
        if b > 0 :
            dfs(n+1,cnt,b-1)

T = int(input())
for tc in range(1,T+1):
    _ = list(map(int,input().split()))
    N,lst = _[0], _[1:]
    ans = N # 모든 정류장에서 교환하는 경우
    dfs(1,0,lst[0]-1)

    print(f'#{tc} {ans}')