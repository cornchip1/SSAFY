import sys
sys.stdin = open('input.txt','r')

def inord(n):

    if n :

        inord(ch1[n])
        alst.append(*lst[n])
        inord(ch2[n])


T = 10
for test_case in range(1,T+1):
    N = int(input()) # 정점의 총 개수
    lst = [[] for _ in range(N+1)]
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)

    for _ in range(N) : # 정점 정보 입력
        data = list(input().split())
        if len(data) == 4:
            p, v, l, r = data[0],data[1],data[2],data[3] # parent, value, left child, right chilrd
            p = int(p); l = int(l); r = int(r)
            lst[p].append(v)
            ch1[p] = l; ch2[p] = r
        elif len(data) == 3 :
            p,v,l = data[0],data[1],data[2]
            p = int(p); l = int(l);
            lst[p].append(v)
            ch1[p] = l
        elif len(data) == 2:
            p,v = data[0],data[1]
            p = int(p)
            lst[p].append(v)

    alst = []; ans = ''

    inord(1)
    for i in alst: ans += i
    print(f'#{test_case}',ans)