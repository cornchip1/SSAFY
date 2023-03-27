import sys
sys.stdin = open('s_input.txt','r')

A = [int(_n) for _n in range(1,13)]

T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split()) # N개의 원소, 원소의 합이 K
    ans = 0 # 부분집합이 없음

    subsets = [[]]
    for a in A :
        n = len(subsets)
        for x in range(n):
            subset = subsets[x]+[a]
            subsets.append(subset)
            if len(subset) == N and sum(subset) == K : ans += 1

    print(f'#{test_case} {ans}')