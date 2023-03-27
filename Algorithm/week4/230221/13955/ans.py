'''
def BFS():
    1. q, v[], 필요한 flag 생성 및 초기화
    2. 초기 단위 작업 - q에 초기 데이터(들) 삽입, v[] 표시/ 필요시 정답 관련 처리
    while q:
    3. q에서 데이터를 1개 꺼냄 (+ 정답 처리/ 가능하면 이 자리에서)
    4. 4/8 방향/연결 노드 ... (반복)
    4-1. 범위 내에 있고, 미방문 좌표이며, 조건에 맞으면 # 2 의 단위 작업 진행
 '''

import sys
sys.stdin = open('s_input.txt','r')

def BFS(s):
    # 1 필요한 변수들 생성
    q = []
    v = [0] * (V+1)

    # 2 단위 작업
    q.append(s)
    v[s] = 1
    alst.append(s)

    # 3 q 에 데이터가 있는 경우에는
    while q :
        # 3-1 데이터를 한 개 꺼낸다
        c = q.pop(0)

        # 3-2 4/8방향/연결된 노드 등 반복 처리
        for n in adj[c] :
            # 범위 내 & 미방문 & 조건 부합 시 (맞으면, 같은 길이면 등등)
            if v[n] == 0 :
                q.append(n)
                v[n] = 1 # 경우에 따라 이전 (v[c] + 1) 인 경우도 있음 - 예를 들면 거리
                alst.append(n)

T = int(input())
for test_case in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[]for _ in range(V+1)]

    for _ in range(E):
        s,e = map(int,input().split())
        adj[s].append(e)
        adj[e].append(s)

    # 인접 리스트 - 번호순이라는 조건이 있다면 반드시 정렬 후 사용
    for lst in adj :
        lst.sort()

    alst = []
    BFS(1)

    print(f'#{test_case}', *alst)
