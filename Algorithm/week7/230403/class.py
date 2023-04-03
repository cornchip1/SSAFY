def dfs1(v,k): # 중복 없이, 빠짐 없이
    visited[v] = 1 # 중복 방지
    print(v)

    for w in adjL[v]:
        if visited[w] == 0 :
            dfs1(w,k)
    # for w in range(1,k+1):
    #     if adjM[v][w] == 1  and visited[w] == 0 :
    #         dfs1(w,k)


# 반복구조 : 스택 활용
def dfs2(v, k):
    stack = []
    visited = [0] * (k + 1)
    while True:
        if visited[v] == 0 :
            print(v)
            visited[v] = 1
        for w in range(1, k + 1):
            if adjM[v][w] and visited[w] == 0:
                stack.append(v)
                v = w
                break
        else:  # 더이상 인접 정점이 없으면
            if stack:  # 비어있지 않으면 그 정점을 꺼낸다
                v = stack.pop()
            else:  # 비어있으면 반복을 종료한다
                break
    return

# 주어진 출발지에서 목적지까지 갈 수 있는 방법의 개수 구하기
def dfs3(v,k,g):
    global cnt
    if v == g :
        cnt += 1 #목적지 도착 횟수
    else:
        visited[v] = 1 # 중복 방지

        for w in range(1,k+1):
            if adjM[v][w] == 1 and visited[w]== 0 :
                dfs3(w,k,g)

        visited[v] = 0


V, E = map(int,input().split())
arr = list(map(int,input().split()))
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1,n2 = arr[i*2],arr[i*2+1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1
    adjL[n1].append(n2)
    adjL[n2].append(n1)

visited = [0]*(V+1) # 중복 방지
# dfs1(1,V)
# dfs2(1,V)
cnt = 0
dfs3(1,V,7)
print(cnt)