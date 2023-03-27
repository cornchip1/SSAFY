import sys
sys.stdin = open('input.txt','r')
T = int(input())

for test_case in range(1,T+1):
    N = int(input()) #number of carrots (= length of list C)
    C = list(map(int,input().split()))

    ans = 1
    cnt = 1

    for i in range(N-1):
        if C[i] < C[i+1] :
            cnt += 1
            if cnt > ans :
                ans = cnt
            else :
                pass
        else :
            cnt = 1
            continue

    print(f'#{test_case} {ans}')