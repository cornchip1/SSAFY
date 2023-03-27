'''
왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.
ㄴ 좌/우 2칸을 확인해서, 나를 제외한 최댓값을 구하고, (내 높이 - 나를 제외한 최대값)의 누적 갯수를 구하면 되는 문제
빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.

       0 1 2 3 4 5 6 7 8 9 10
lst = [0,0,3,5,2,4,9,0,6,0,0]
           ^           ^
           i           i
ans = 0                                     # 초기값
for j (2,N-2) :                             # i 의 범위: 2 ~ N-2  -> 기준
    mx = lst[i-2]                           # 첫번째 값을 최댓값이라고 가정한다
    for j(i-1, i+2+1)                       # i 양옆 2칸씩 확인, mx를 초기값으로 지정했으므로 i-2제외
        if i == j : continue                # i 는 제외
        else :
            if mx < lst[j] : mx = lst[j]    # 더 큰 값으로 mx 업데이트
    if lst[i] > mx :
        ans += (lst[i] - mx)
'''

import sys
sys.stdin = open('s_input.txt','r')

T = 3
for test_case in range(1,T+1) :
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    M = 2               # 고정값이 아닌 일반화

    for i in range(M,N-M) :
        mx = lst[i-M]       #max(lst[i-M:i] + lst[i+1:i+M+1) // ans = max(0, lst[i] - mx)
        for j in range(i-M+1, i+M+1) :
            if i == j :
                continue    #기준값을 제외한 값 중 최댓값을 찾는다
            else :
                if mx < lst[j] :
                    mx = lst[j]     #mx 값 갱신
        if lst[i] > mx :            #기준값이 가장 크면 조망권 있음
            ans += lst[i]-mx


    print(f'#{test_case} {ans}')
