import sys
sys.stdin = open('input (3).txt','r')

T = int(input())
for test_case in range(1,T+1):
    st = input()
    lst = []
    for s in st :
        if s.isdigit() == 0 :
            lst.append(ord(s)-55)
        else: lst.append(int(s))

    t = ''
    for i in lst :
        bin = []
        while True :
            if i == 0 : bin.insert(0,'0') ; break
            else:
                bin.insert(0,str(i % 2))
                i = i//2
        t += ''.join(bin)

    alst = []
    for n in range(2,len(t)-2,7)

    print(f'#{test_case}',)