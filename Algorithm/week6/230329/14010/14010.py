import sys
sys.stdin = open('s_input.txt','r')

def ftn(l,r,m):
    global lcnt, rcnt, ans

    if l >= r:
        return

    for b in B:
        if b == A[m]:
            lcnt += 1
            rcnt += 1
            ans += 1
        elif b < A[m]:
            r = m-1
            m = (l + r) // 2
            lcnt += 1
            if b == A[m] and rcnt >= 1: ans += 1
            ftn(l,r,m)
        else:
            l = m + 1
            m = (l + r) // 2
            rcnt += 1
            if b == A[m] and lcnt >= 1: ans += 1
            ftn(l,r,m)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    A,B = [list(map(int,input().split())) for _ in range(2)]
    l,r = 0,N-1
    m = (l+r)//2

    A.sort()
    ans,lcnt,rcnt = 0, 0, 0
    ftn(l,r,m)

    print(f'#{tc} {ans}')