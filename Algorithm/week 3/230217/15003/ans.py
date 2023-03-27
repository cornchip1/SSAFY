import sys
sys.stdin = open('s_input (1).txt','r')
T = int(input())
for test_case in range(1,T+1):
    st = '0' + input()
    ans = 0
    # len 을 쓰는 경우 - N이 안주어졌거나 바뀔 수 있는 경우
    for i in range(1,len(st)):
        if st[i-1] != st[i] : ans += 1
    print(f'#{test_case} {ans}')
