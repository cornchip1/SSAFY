N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

# 1 아기 상어의 위치와 물고기들의 위치 파악
fishes = []
si,sj = 0,0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9 : si,sj = i,j
        elif arr[i][j] != 0 : fishes.append([i,j,0])


# 2 물고기들과 아기상어와의 거리 구하기
size = 2 # 아기상어의 처음 크기는 2

# 거리 계산 함수
from collections import deque
def cal(si,sj,fi,fj):
    q = deque()
    q.append((si,sj))

    v = [[0]*N for _ in range(N)]
    v[si][sj] = 1

    while True:
        ci,cj = q.popleft()

        # 2-1 종료 조건
        if (ci,cj) == (fi,fj):
            # 최소 distance 반환
            return(v[ci][cj] -1)

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] <= size and v[ni][nj] == 0:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni,nj))

for f in fishes: # 아기상어와 거리 계산
    fi,fj = f[0],f[1]
    f[2] = cal(si,sj,fi,fj)

# 3 아기 상어의 물고기 사냥


print(fishes)