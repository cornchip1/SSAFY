N = int(input())
tri = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,N):
    for j in range(len(tri[i])):
        if j  == 0 : tri[i][j] = tri[i-1][j] + tri[i][j]
        elif j == len(tri[i])-1 : tri[i][j] = tri[i-1][j-1] + tri[i][j]
        else: tri[i][j] = max(tri[i-1][j],tri[i-1][j-1]) + tri[i][j]

# print(tri)
print(max(tri[N-1]))