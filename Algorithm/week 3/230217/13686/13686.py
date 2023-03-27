import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # 일 수
    lst = list(map(int,input().split()))

    # 단위 연산
    # 1 최대값 구하기
    mx = 0
    for _ in lst :
        if _ > mx : mx = _

    # 2 최대값을 기준으로 리스트 분리
    stk = []
    for p in lst :
        if p >= mx : stk.append(lst.pop(p))

    print(stk,lst)
