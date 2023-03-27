import sys
sys.stdin = open('s_input.txt','r')

def ST(N):

    if ch1[N] :
        alst.append(ch1[N])
        ST(ch1[N])
    if ch2[N]:
        alst.append(ch2[N])
        ST(ch2[N])

    return len(alst)

T = int(input())
for test_case in range(1,T+1):
    E, N = map(int,input().split()) # E: 간선의 개수 N: root
    lst = list(map(int,input().split()))

    ch1 = [0] * (E+2) ; ch2 = [0] * (E+2)

    for i in range(0,len(lst),2):
        p,c = lst[i],lst[i+1]
        if ch1[p] == 0 : ch1[p] = c
        else: ch2[p] = c

    alst = [N]

    print(f'#{test_case} {ST(N)}')