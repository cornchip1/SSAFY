# def dfs(n,sm,value):
#     global ans
#
#
#     if n == N or sm >= K:
#         if sm <= K :
#             ans = max(ans,value)
#         return
#
#
#     for i in range(N):
#         if v[i] == 0 :
#             v[i] = 1
#             dfs(n+1,sm+lst[i][0],value+lst[i][1])
#             v[i] = 0
#
# N, K = map(int,input().split())
# lst = [tuple(map(int,input().split())) for _ in range(N)]
#
# v = [0]*N
# ans = 0
#
# dfs(0,0,0)
#
# print(ans)


N, K = map(int,input().split())
lst = [tuple(map(int,input().split())) for _ in range(N)]

v = [0]*N
ans = 0

tmp = []
for i in range(N-1):
    for j in range(i,)


