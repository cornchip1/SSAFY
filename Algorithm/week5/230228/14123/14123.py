import sys
sys.stdin = open('input (1).txt','r')
T = int(input())
for test_case in range(1,T+1):
    st = input()
    sts = []
    for s in range(0,len(st),7) :
        sts.append(st[s:s+7])

    alst = []
    for i in sts :
        x = 0
        # 0000111
        for n in range(6,-1,-1):
            if i[n] == '1' : x += 2**(6-n)
        alst.append(x)

    print(f'#{test_case}',*alst)