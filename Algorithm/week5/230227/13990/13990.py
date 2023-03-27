import sys
sys.stdin = open('s_input1.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    N = float(input())

    bin = []
    n = 1
    while True:
        if N == 0 :
            if len(bin) == 0 :
                bin.append('0')
            break
        else:
            if N-(2**-n) >= 0 :
                bin.append('1')
                N = N - (2**-n)
                n += 1
            else: bin.append('0') ; n += 1

    if len(bin) > 13 : ans = 'overflow'
    else : ans = ''.join(bin)

    print(f'#{test_case} {ans}')
