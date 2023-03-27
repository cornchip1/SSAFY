import sys
sys.stdin = open('s_input.txt','r')

T = int(input())

for test_case in range(1, T+1) :
    N, M = map(int, input().split()) #N : 입력된 숫자의 갯수 M : 더하는 숫자의 갯수
    data = list(map(int,input().split())) #입력되는 숫자 배열
    sums = [0]*(N-M+1) #배열에서 M개 숫자의 합의 경우의 수

    for i in range(N-M+1):
        n_sum = 0
        for j in range(i,i+M):
            n_sum += data[j]
        sums[i] = n_sum

    for x in range(len(sums)):
        for y in range(x+1, len(sums)):
            if sums[x] > sums[y] :
                sums[x],sums[y] = sums[y],sums[x]

    diff = sums[-1] - sums[0]

    print(f'#{test_case} {diff}')