import sys
sys.stdin = open('s_input1.txt','r')

T = int(input())
for tc in range(1,T+1):
    num = float(input())

    tmp = []
    n = 1 # 0보다 크고 1 미만 // 2**0 일 수 없음
    while True: # 0.625
        x = num - 2**(-n)
        if num == 0 :
            break
        if x >= 0 :
            tmp.append('1')
            num = x
        else:
            tmp.append('0')
        n += 1

    if tmp:
        if len(tmp) > 13 : ans = 'overflow'
        else: ans = ''.join(tmp)
    else: ans = 0

    print(f'#{tc} {ans}')