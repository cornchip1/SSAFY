import sys
sys.stdin = open('s_input.txt', 'r')
# 16진수: 0 1 2 3 4 5 6 7 8 9 A B C D E F
T = int(input())
for test_case in range(1,T+1):
    N,st = input().split()
    st = list(_ for _ in st)
    ans = ''

    for i in range(int(N)):
        if st[i].isdigit(): st[i] = int(st[i])
        else:
            if st[i] == 'A' : st[i] = 10
            elif st[i] == 'B' : st[i] = 11
            elif st[i] == 'C' : st[i] = 12
            elif st[i] == 'D' : st[i] = 13
            elif st[i] == 'E' : st[i] = 14
            elif st[i] == 'F' : st[i] = 15


    for n in st:
        bin = []
        while True:
            if n == 0 : break
            else:
                bin.insert(0,str(n%2))
                n = n // 2
        if len(bin) < 4:
            for x in range(4-len(bin)):
                bin.insert(0,'0')
        ans += ''.join(bin)


    print(f'#{test_case} {ans}')

    # 1 0100011111111110
    # 2 0111/1001/1110/0001/0010
    # 2 0111/1001/1110/0001/0010

    # 3 0100/0001/1101/1010/0001/0110/1100/1101
    # 3 0100/0001/1101/1010/0001/0110/1100/1101