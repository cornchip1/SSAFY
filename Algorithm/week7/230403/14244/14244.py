import sys
sys.stdin = open('s_input.txt','r')

def bfs(s,e):

    # [1] q,v 생성
    q = [0]*1000000
    v = [0]*1000001
    w = r = 0

    # [2] q에 초기 데이터 삽입
    q[w] = s
    w = (w+1)%1000000
    v[s] = 1

    while w != r :
        c = q[r]
        r = (r+1) % 1000000
        if c == e :
            return v[e]-1

        for n in ((c-1),(c+1),(c*2),(c-10)):
            if 1 <= n <= 1000000 and v[n] == 0 :
                q[w] = n
                w = (w+1) % 1000000
                v[n] = v[c] + 1
    return -1

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())

    ans = bfs(N,M)

    print(f'#{tc} {ans}')