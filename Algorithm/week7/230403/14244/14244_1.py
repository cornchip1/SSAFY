import sys
sys.stdin = open('s_input.txt','r')

def bfs(s,e):
    q = [0] * 1000000
    v = [0] * 1000001
    i = j = 0

    q[i] = s
    v[s] = 1
    i += 1

    while i != j :
        c = q[j] # 직전 값
        j += 1
        if c == e : # 정답 처리
            return v[e]-1 # 확인용
        for n in ((c+1),(c-1),(c*2),(c-10)):
            if 1 <= n <= 1000000 and v[n] == 0 :
                q[i] = n
                v[n] = v[c] + 1
                i += 1

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())

    ans = 1000000
    bfs(N,M)

    print(f'#{tc} {bfs(N,M)}')