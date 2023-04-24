# from itertools import permutations
#
# N,M = map(int,input().split())
# lst = [ _ for _ in range(1,N+1)]
#
# clst = permutations(lst,M)
# for c in clst:
#     print(*c)


def dfs(n,lst):
    if n == M :
        alst.append(lst)
        return

    for j in range(1,N+1):
        if v[j] == 0 :
            v[j]=1
            dfs(n+1,lst+[j])
            v[j]=0

N,M = map(int,input().split())
alst = []
v = [0]*(N+1)
dfs(0,[])

for a in alst:
    print(*a)