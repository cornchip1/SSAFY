import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split()) # N : 수열의 크기, M : 맨 앞의 숫자를 맨 뒤로 보내는 횟수
    nlst = list(map(int,input().split()))

    m = 0
    while m < M :
        nlst.append(nlst.pop(0))
        m += 1

    print(f'#{test_case} {nlst[0]}')