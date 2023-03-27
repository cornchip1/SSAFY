import sys
sys.stdin = open('s_in.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N, D = map(int,input().split()) # N : 배열의 갯수, D : 찾을 숫자
    lst = list(map(int,input().split()))
    ans = 0 # 첫번째 위치가 1이므로, 초기값을 1로 설정한다

    start, end = 0, N-1
    while start <= end :
        middle = (start+end)//2
        if lst[middle] == D:
            ans = middle +1
            break
        elif lst[middle] > D :
            end = middle -1
        elif lst[middle] < D :
            start = middle + 1
        else :
            ans = 0


    print(f'#{test_case} {ans}')