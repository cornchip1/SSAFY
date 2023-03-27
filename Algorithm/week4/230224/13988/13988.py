import sys
sys.stdin = open('sample_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # 1 <= N <= 10**18
    for i in range(1,10**6+1):
        if i**3 == N :
            x = i
            break
        elif i **3 > N :
            x = -1
            break
        else : x = -1
    print(f'#{test_case} {x}')