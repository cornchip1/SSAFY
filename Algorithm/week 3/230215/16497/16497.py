import sys
sys.stdin = open('input.txt','r')
T = 10
for test_case in range(1,T+1):
    N = int(input()) # 계산식의 길이
    eq = input()

    # 후위 표기식으로 변환
    stk = []
    alst = []
    for i in eq :
        if i.isdigit() : alst.append(i) # 숫자라면 alst에 더한다
        else : # '+' 라면
            while stk :   # stk 이 비어있지 않으면
                alst.append(stk.pop()) # alst 에 stk의 마지막 '+'를 더한다
            stk.append(i)  # stk에 '+' 를 더한다
    while stk : # stk 에 남아있는 마지막 '+' 를 alst에 더한다
        alst.append(stk.pop())

    # 후위 표기식 계산
    cstk = [] # 계산을 위한 stk 생성
    for i in alst :
        if i.isdigit() : cstk.append(int(i)) # 숫자라면 cstk에 더한다
        else : # i가 '+'이면
            if cstk : # cstk이 비어있지 않다면
                cstk.append(cstk.pop() + cstk.pop()) # 마지막 두 원소를 더하여 cstk에 다시 넣는다

    ans = cstk[0] # 정상적인 연산이 완료됐다면 cstk의 원소는 하나일 것이므로, cstk의 첫번째 원소가 답이 된다

    print(f'#{test_case} {ans}')
