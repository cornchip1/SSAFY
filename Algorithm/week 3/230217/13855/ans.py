import sys
sys.stdin = open('input.txt','r')
priority = {'(':0,'+':1,'*':2}

T = 10
for test_case in range(1,T+1):
    _ = int(input())
    str = input()
    ans = 0

    # 1 중위표기식을 후위표기식으로 변환
    stk = []
    eq = ''
    for ch in str :
        if ch.isdigit() : eq += ch # 숫자면 eq에 추가
        else :
            if ch == '(' : stk.append(ch) # '(' 이면 무조건 스택에 추가
            elif ch == ')' : # ')' 이면 열리는 괄호를 만날 때까지 모두 pop, eq에 추가
                while stk[-1] != '(':
                    t = stk.pop()
                    if t == '(' : break # 괄호연산 완료
                    else : eq += t
                stk.pop()
            else : # 괄호가 아니라면 기존 연산 수행
                while stk and priority[ch] <= priority[stk[-1]] :
                    eq += stk.pop()
                stk.append(ch)

    while stk :
        eq += stk.pop()

    # 2 후위표기식 연산
    for ch in eq :
        if ch.isdigit() : stk.append(int(ch)) # 숫자라면
        else : # 연산자라면
            if len(stk) >= 2 : # 연산자가 두개 다 있으면
                if ch == '+' : stk.append(stk.pop()+stk.pop())
                elif ch == '*' : stk.append(stk.pop()*stk.pop())
                else : ans = -1
            else : ans = -1
    if ans != -1 : ans = stk.pop()

    print(f'#{test_case} {ans}')