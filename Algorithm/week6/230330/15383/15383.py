import sys
sys.stdin = open('s_input.txt','r')

def dfs(n,lst):
    global alst

    # 가지치기 // 중복값을 제거하여 실행 시간을 줄이고, 정답을 마지막에 확인함
    tmp = int(''.join(lst))
    if tmp not in alst[n]:
        alst[n].append(tmp)
    else: return
    # N 회 반복
    if n == N :
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
    alst = [[] for _ in range(N+1)]


    v = [0]*N
    ans = 0
    dfs(0,lst)
    print(f'#{tc} {max(alst[N])}')
