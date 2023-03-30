import sys
sys.stdin = open('s_input.txt','r')

'''def calc(alst):
    result = alst[0]
    for i in range(1,N*2-2,2):
        if alst[i] == '+' : result += alst[i+1]
        elif alst[i] == '-' : result -= alst[i+1]
        elif alst[i] == '*' : result *= alst[i+1]
        elif alst[i] == '/' : result = int(result/alst[i+1])
    return result

def dfs(i,l,o,alst):
    global mx,mn
    if i == N*2-1 :
        ans = calc(alst)
        mx = max(ans,mx)
        mn = min(ans,mn)
        return
    if i % 2 :
        for o in range(N-1):
            if vop[o] == 0 :
                vop[o] = 1
                dfs(i+1,l,o+1,alst+[op[o]])
                vop[o] = 0
    else:
        dfs(i+1,l+1,o,alst+[lst[l]])'''


def dfs(n,result):
    global mx, mn
    if n == N-1 :
        mx = max(result,mx)
        mn = min(result,mn)
        return
    if op[0]:
        op[0] -= 1
        dfs(n+1,result + lst[n+1])
        op[0] += 1
    if op[1]:
        op[1] -= 1
        dfs(n + 1, result - lst[n + 1])
        op[1] += 1
    if op[2]:
        op[2] -= 1
        dfs(n + 1, result * lst[n + 1])
        op[2] += 1
    if op[3]:
        op[3] -=1
        dfs(n + 1, int(result / lst[n + 1]))
        op[3] += 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    op = list(map(int,input().split())) # +,-,*,/ 개수
    lst = list(map(int,input().split())) # 숫자

    mx,mn = -1000000000, 1000000000
    dfs(0,lst[0])

    print(f'#{tc} {mx-mn}')