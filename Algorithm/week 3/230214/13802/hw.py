def DFS(S):
    v = [0] * 100
    stk = []

    s = S
    v[s] = 1
    alst.append(s)

    while True:
        for e in adj[s]:  # 연결된 노드
            if v[e] == 0:  # 미방문 노드
                stk.append(s)
                s = e
                v[s] = 1
                alst.append(s)
                break  # 탐색 종료
        else:  # 연결되지 않은 노드
            if stk:
                s = stk.pop()  # stk이 비어있지 않으면 s = 마지막 원소
            else:
                break


def my_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        minidx = i
        for j in range(i + 1, n):
            if lst[minidx] > lst[j]:
                minidx = j
        lst[i], lst[minidx] = lst[minidx], lst[i]
    return lst


T = 10
for test_case in range(1, T + 1):
    S, E = 0, 99
    _tc, _N = map(int, input().split())  # _tc: test case no, _N: 길의 총 개수
    lst = list(map(int, input().split()))  # 경로의 순서쌍
    unique = []  # unique 노드들을 받기 위한 list

    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] not in unique:
            unique.append(lst[i])

    my_sort(unique)

    adj = [[] for _ in range(100)]

    for i in range(len(lst) - 1):
        if i % 2 == 0:
            adj[lst[i]].append(lst[i + 1])
        my_sort(adj[lst[i]])

    alst = []  # 노드들의 이동 경로
    DRS(S)

    ans = 0
    if E in alst:  # 만약 이동 경로 안에 G가 있다면 A 도시에서 B 도시로 가는 길이 있는 것이다
        ans = 1

    print(f'#{test_case} {ans}')