import sys
sys.stdin = open('s_input.txt','r')

def find_set(n):
    if n == p[n] :
        return n
    p[n] = find_set(p[n])
    return p[n]

def union(s,e):
    p[find_set(e)] = find_set(s)

def Kruskal():
    arr.sort(key = lambda x : x[2])
    # [2] V 개의 링크를 선택
    ret = cnt = 0
    for (s,e,w) in arr :
        if find_set(s) != find_set(e):
            union(s,e)
            ret += w
            cnt += 1
            if cnt == V : return ret # 노드개수 - 1개를 연결하면 종료

    return -1

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]

    # [1] make_set() : 각자 자기가 대표인 그룹 생성
    p = [n for n in range(V+1)]

    ans = Kruskal()
    print(f'#{tc} {ans}')