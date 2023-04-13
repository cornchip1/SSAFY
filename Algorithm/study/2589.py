N,M = map(int,input().split())
arr = [[_n for _n in input()] for _ in range(N)]

land = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L' : land.append((i,j))

from itertools import combinations
com = combinations(land,2)

def search(si,sj,ei,ej):

    v = [[0]*M for _ in range(N)]
    ci,cj = si,sj
    v[ci][cj] = 1
    distance = 0

    while True:

        sea = 0
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if (ni,nj) == (ei,ej): return distance
            if sea == 4: return -1
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0:
                if arr[ni][nj] == 'L':
                    v[ni][nj] = 1
                    distance += 1
                elif arr[ni][nj] == 'W':
                    sea += 1




ans = 0
for c in com :
    c = list(c)
    si,sj,ei,ej = c[0][0],c[0][1],c[1][0],c[1][1]
    res = search(si,sj,ei,ej)
    ans = max(res,ans)

print(ans)