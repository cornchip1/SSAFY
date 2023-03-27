import sys
sys.stdin = open('input.txt','r')

# 스택에 들어올 때 priority // incoming '(' 는 가장 높은 우선순위 : 무조건 stack 에 push
icp = {'(':3,'+':1,'*':2}
# 스택 안에 있을 때 priority // in stack '(' 는 가장 낮은 우선순위 : 그래야 ')' 이 나올때까지 stack 에서 pop 되지 않음
isp = {'(':0,'+':1,'*':2}


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
            if ch == ')' : # ')' 이면 열리는 괄호를 만날 때까지 모두 pop, eq에 추가
                while stk[-1] != '(':
                    t = stk.pop()
                    if t == '(' : break # 괄호연산 완료
                    else : eq += t
                stk.pop()
            else : # 괄호가 아니라면 기존 연산 수행
                while stk and icp[ch] <= isp[stk[-1]] :
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