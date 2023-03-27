'''
for 문 안에 또다른 for 문이 들어가게 되면, 연산을 더 많이 하게 됨

더 효율적인 방법을 찾는다면?
-> ith 합을 구하면 첫 값을 제외하고, 그 뒤의 첫 값을 추가하여 합을 계산한다

아래는 그 방법
'''

import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1) :

    N,M = map(int, input().split())  # N : 입력된 숫자의 갯수 M : 더하는 숫자의 갯수
    lst = list(map(int, input().split()))  # 입력되는 숫자 배열

    mn = M*10000
    mx = 0
    sm = 0

    for i in range(M) :
        sm += lst[i]

    mn = mx = sm
    for i in range(M,N) :
        sm += lst[i]   #i 위치 값 추가
        sm -= lst[i-M] #i-M 위치 값 제거
        if mx < sm :
            mx = sm
        if mn > sm :
            mn = sm

    ans = mx - mn

    print(f'#{test_case} {ans}')


