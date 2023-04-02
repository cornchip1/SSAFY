import sys
sys.stdin  = open('input (2).txt','r')

def bin(i,tlst):
    if i > 0 :
        x,y = divmod(i,2)
        if x >= 2 :
            tlst.insert(0,str(y))
            bin(x,tlst)
        else:
            tlst.insert(0,str(y))
            tlst.insert(0,str(x))
    else :
        tlst.append('0')

    if len(tlst) < 4 :
        for _ in range(4-len(tlst)):
            tlst.insert(_,'0')

    res = ''.join(tlst)
    return res

def dec(num):
    a = 0
    for j in range(len(num)):
        a += int(num[j]) * 2 ** (len(num)-j-1)
    return a

T = int(input())
for tc in range(1,T+1):
    st = input()

    tmp = []
    for i in st:
        if i.isdigit(): tmp.append(int(i))
        else:
            tmp.append(ord(i)-ord('A')+10)

    bins = ''
    for t in tmp:
        bins += bin(t,[])

    alst = []
    for i in range(0,len(bins),7):
        num = bins[i:i+7]
        alst.append(dec(num))

    print(f'#{tc}', *alst)