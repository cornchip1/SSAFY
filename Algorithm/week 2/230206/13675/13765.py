import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1) :
    N, K = map(int,input().split())
    A = [a for a in range(1,13)]
    ans = 0

    for bit in range(1<<len(A)):
        sm, cnt = 0,0
        for j in range(len(A)):
            if bit&(1<<j):
                sm += A[j]
                cnt += 1
        if sm == K and cnt == N:
            ans += 1

    print(f'#{test_case} {ans}')