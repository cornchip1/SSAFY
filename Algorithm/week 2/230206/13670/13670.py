import sys
sys.stdin = open('s_in2.txt','r')

T = int(input())
for test_case in range(1,T+1):
    lst = list(map(int,input().split()))
    N = len(lst)
    ans = 0

    for i in range(1, 1<<N) : #공집합을 제외해야 부분집합의 합이 0인 부분집합들의 개수를 제대로 셀 수 있음
        s = 0
        for j in range(N):
            if i & (1<<j) :
                s += lst[j]
        if s == 0 :
            ans = 1
            break
    print(f'#{test_case} {ans}')