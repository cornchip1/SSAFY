# 거듭제곱
import sys
sys.stdin = open('input.txt','r')

def mul(n,m):
    while m > 0 :
        m -= 1
        return n*n


T = 10
for test_case in range(1,T+1):
    _ = int(input())
    N, M = map(int,input().split())

    ans = mul(N,M)

    print(f'#{test_case} {ans}')