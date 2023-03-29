import sys
sys.stdin = open('s_input.txt','r')

def bs(s,e,d):
    dr = 0
    while s <= e :
        m = (s+e)//2
        if lst[m] == d : return 1
        elif lst[m] < d :
            if dr == 1 : return 0
            dr = 1
            s = m+1
        else :
            if dr == -1 : return 0
            dr = -1
            e = m-1
    return 0

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    lst,lst2 = [list(map(int,input().split())) for _ in range(2)]
    lst.sort()

    ans = 0
    for d in lst2:
        ans += bs(0,N-1,d)
    print(f'#{tc} {ans}')
