import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N,P = map(int,input().split())

    n = 0
    ans = 0


    i = 1
    while 1 <= i < N-i :
        lst = [0] * P
        mul = 1
        for p in range(P-1):
            lst[p] = i
            i += 1
        if N-sum(lst[:p+1]) > 0 : lst[-1] = N - sum(lst[:p+1])
        print(lst)
        for l in lst :
            mul *= l
        if mul > ans : ans = mul

        i += 1

    print(f'#{test_case} {ans}')

