# 이진 탐색을 사용해서 찾는 문제
import sys
sys.stdin = open('sample_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    s, e = 1, N
    ans = -1
    while s <= e :
        m = (s+e)//2
        # 발견 시
        if m**3 == N : ans = m ; break
        elif m**3 < N : s = m+1
        else : e = m-1
    print(f'#{test_case} {ans}')

''' 
변형 이진탐색
s - - - - - m - - ans - - e
s, e 가 주어졌는데, 조건을 만족하는 최대값을 구해라!

while s <= e :
    m = (s+e)//2 
    # m 이 최대값일수도 있어서 우선 ans 에 m을 저장한다
    if check(m, - ) == True : 
        ans = m 
        s = m+1
    else : # check(m, - ) == False // 조건을 만족하지 못하면
        e = m-1 

'''
