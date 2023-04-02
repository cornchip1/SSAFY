import sys
sys.stdin = open('s_input.txt','r')

def bin(n,res):

    x,y = divmod(n,2)

    if x >= 2 : 
        res.insert(0,str(y))
        bin(x,res)
    else :
        res.insert(0,str(y))
        res.insert(0,str(x))

    return res

T = int(input())
for tc in range(1,T+1):
    N, num = input().split()
    N = int(N)

    tmp = []
    for i in num :
        if i.isdigit() :
            tmp.append(int(i))
        else:
            tmp.append(ord(i)-ord('A')+10)

    ans = []
    for n in tmp :
        b = bin(n,[])
        if len(b) < 4 :
            for _ in range(4-len(b)):
                b.insert(0,'0')
        ans += b

    ans = ''.join(ans)

    print(f'#{tc} {ans}')