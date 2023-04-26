from itertools import combinations

def total_distance(houses, chicken):
    td = 0
    for n in houses:
        distance = N**2
        for c in chicken:
            d = abs(houses[n][0] - chicken[c][0]) + abs(houses[n][1] - chicken[c][1])
            distance = min(distance, d)
        td += distance

    return td


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 1 치킨집 리스트 구하기
chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2 : chickens.append((i,j))
        elif arr[i][j] == 1 : houses.append((i,j))

# 2 남기는 치킨집의 모든 경우의 수 구하기
md = 0
for chicken in list(combinations(chickens,M)):
    md = min(total_distance(houses, chicken),md)

print(md)