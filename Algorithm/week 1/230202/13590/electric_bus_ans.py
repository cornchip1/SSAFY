import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1) :
    K, N, M = map(int,input().split())
    lst = [0] + list(map(int,input().split())) + [N] #시작 정류장과 종점을 더한다
    ans = s = 0 #시작점(s) 와 충전 횟수(ans) 의 initial value = 0

    for i in range(1, len(lst)) :
        #정류장 사이가 K 이상인 경우 : 종점까지 도달 불가능
        if lst[i] - lst[i-1] > K :
            ans = 0
            break
        #기준점(start)에서 현재 위치가 이동 불가능한 경우 : 충전
        if lst[i] - lst[s] > K :
            ans += 1
            s = i-1

    print(f'#{test_case} {ans}')