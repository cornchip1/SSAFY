import sys
sys.stdin = open('input.txt','r')

def bfs(s):
    # 0 q,v, 필요한 flag 생성
    q = []
    v = [0]*101
    ans = s

    #1 q에 초기데이터(들) 삽입, v표시
    q.append(s)
    v[s]= 1

    # 2 q가 비어있지 않다면
    while q :
        c = q.pop(0) # 2-1 q에서 한 개 꺼냄 + 필요시 정답 처리
        if v[ans] < v[c] or v[ans] == v[c] and ans<c: # 2-2 정답 처리
            ans = c
        # 3 4/8/연결방향 등 반복 처리
        for n in adj[c]: # n : next / c : current
            if v[n] == 0 : # 미방문 시
                q.append(n)
                v[n] = v[c] + 1 # 현재 값 + 1

    return ans

T = 10
for test_case in range(1,T+1):
    N, S = map(int,input().split())
    lst = list(map(int,input().split()))

    # 1 인접리스트에 연결 저장
    adj = [[] for _ in range(101)]
    for i in range(0,len(lst),2):
        s,e = lst[i],lst[i+1]
        adj[s].append(e)

    ans = bfs(S)
    print(f'#{test_case} {ans}')