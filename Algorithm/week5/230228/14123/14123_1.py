import sys
sys.stdin = open('input (1).txt','r')

def dec(num):
    res = 0
    for n in range(7):
        res += int(num[n])*2**(7-n-1)
    return res

T = int(input())
for tc in range(1,T+1):
    st = input()
    alst = []
    for i in range(0,len(st),7):
        num = st[i:i+7]
        alst.append(dec(num))

    print(f'#{tc}',*alst)