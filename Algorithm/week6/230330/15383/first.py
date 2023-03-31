# 시간초과

import sys
sys.stdin = open('s_input.txt','r')

def dfs(n,lst):
    global ans

    result = int(''.join(lst))

    if n == N :
        ans = max(ans,result)
        print(ans)
        return

    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            lst[i],lst[j] = lst[j],lst[i]
            dfs(n+1,lst)
            lst[i],lst[j] = lst[j],lst[i]

T = int(input())
for tc in range(1,T+1):
    _, N = input().split()
    lst = [_i for _i in _]
    N = int(N)

    v = [0]*N
    ans = 0
    dfs(0,lst)
    print(f'#{tc} {ans}')