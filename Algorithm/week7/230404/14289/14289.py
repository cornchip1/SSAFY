import sys
sys.stdin = open('s_input.txt','r')


# [2] find set : x 를 포함하는 집합을 찾는 연산
def find_set(x):
    if x == p[x]: return x
    p[x] = find_set(p[x])
    return p[x]

# [3] union two sets
def union(x,y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))

    p = [n for n in range(N+1)]
    for i in range(M):
        x = lst[2*i]
        y = lst[2*i+1]
        union(x,y)

    result = set()
    for j in range(len(p)):
        if j != 0 :
            result.add(find_set(j))

    print(f'#{tc} {len(result)}')