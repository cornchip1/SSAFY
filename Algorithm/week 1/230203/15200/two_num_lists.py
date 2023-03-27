import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1) :
    N, M = map(int,input().split()) # N : length of list A, M : length of list B
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    n = m = 0

    # 길이가 짧은 리스트를 기준으로 한다
    if N <= M :
        sms = [0]
        while m <= M-N :
            sm = 0
            for i, j in zip(range(N),range(m,M-(M-N)+m)):
                product = A[i] * B[j]
                sm += product
            if sms[0] < sm:
                sms[0] = sm
            else :
                pass
            m += 1

    else :
        sms = [0]
        while n <= N-M:
            sm = 0
            for i, j in zip(range(n,N-(N-M)+n),range(M)):
                product = A[i] * B[j]
                sm += product
            if sms[0] < sm:
                sms[0] = sm
            else:
                pass
            n += 1

    print(f'#{test_case}', *sms)