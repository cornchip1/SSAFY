import sys
sys.stdin = open('input (3).txt','r')

dic = {'001101':0,'010011':1,'111011':2,'110001':3,'100011':4,'110111':5,'001011':6,'111101':7,'011001':8,'101111':9}

def bin(n,tmp):

    x, y = divmod(n,2)
    if x >= 2 :
        tmp.insert(0,str(y))
        bin(x,tmp)
    else:
        tmp.insert(0,str(y))
        tmp.insert(0,str(x))

    if len(tmp) < 4:
        for _ in range(4-len(tmp)):
            tmp.insert(0,'0')

    tmp = ''.join(tmp)
    return tmp

T = int(input())
for tc in range(1,T+1):
    st = input()

    tlst = []
    for s in st :
        if s.isdigit(): tlst.append(int(s))
        else: tlst.append(ord(s)-ord('A')+10)

    bst = ''
    for t in tlst:
        bst += bin(t,[])

    ei = 0
    for i in range(len(bst)-1,-1,-1):
        if bst[i] == '1':
            ei = i
            break

    alst = []
    for ci in range(ei+1,len(bst)%6+1,-6):
        alst.insert(0,(dic[bst[ci-6:ci]]))

    print(f'#{tc}',*alst)