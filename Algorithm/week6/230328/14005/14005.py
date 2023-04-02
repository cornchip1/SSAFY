import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    W = list(map(int,input().split()))
    V = list(map(int,input().split()))

    W.sort(reverse=True)
    V.sort(reverse=True)

    ans = 0
    vi = [0]*N
    vj = [0]*M

    for i in range(N):
        for j in range(M):
            if vi[i] == 0 and vj[j] == 0 :
                if W[i] <= V[j] :
                    vi[i] = 1
                    vj[j] = 1
                    ans += W[i]

    print(f'#{tc} {ans}')