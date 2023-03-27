import sys
sys.stdin = open('input.txt','r')

T = 10
for test_case in range(1,T+1):
    N = int(input()) # 건물의 개수
    lst = list(map(int,input().split()))
    ans = 0

    for i in range(2,N-2): # 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다
        check = []
        for di in (-2,-1,1,2):
            ni = i+di
            if lst[ni] < lst[i] :
                check.append(lst[i]-lst[ni])
        if len(check) == 4 : ans += min(check)

    print(f'#{test_case} {ans}')