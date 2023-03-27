import sys
sys.stdin = open('input.txt','r')

priority = {'(':1,'+':2,'*':3}
def pn(st) :
    stk, eq = [],''
    for ch in st :
        if ch.isdigit(): eq += ch # 숫자면 eq에 넣는다
        else : # 연산자이면
            if stk:  # stk 이 비어있지 않으면
                if ch == '(' : stk.append(ch) # '(' 면 무조건 넣는다
                elif ch == ')' : # ')' 라면
                    while stk[-1] != '(' : # stk 에 있는 연산자가 '(' 이 아니라면
                        eq += stk.pop() # stk 에서 빼내서 eq에 더한다
                    stk.pop() # 남아있는 '(' 제거
                else: # 괄호가 아니라면
                    if priority[ch] >= priority[stk[-1]] : # 우선순위가 stk의 마지막 연산자의 우선순위보다 높다면
                        stk.append(ch) # stk 에 넣는다
                    else : # 마지막 연산자의 우선순위보다 낮다면
                        while stk and priority[ch] <= priority[stk[-1]] : # stk 이 비어있지 않고 stk의 마지막 연산자의 우선순위가 현재 연산자보다 크거나 같을 동안
                            eq += stk.pop() # stk의 마지막 연산자를 eq에 더한다
                        stk.append(ch) # 현재 연산자를 stk 에 넣는다
            else : stk.append(ch) # stk이 비어있으면 연산자를 더한다
    while stk :
        if stk[-1] == '(' : stk.pop()
        else: eq += stk.pop() # stk에 남아있는 연산자가 있으면 eq에 더한다

    return eq

def calc(eq) :
    stk = []
    for ch in eq :
        if ch.isdigit() : stk.append(int(ch)) # 숫자면 stack에 넣는다
        else: # 연산자이면 두개를 뽑아서 연산 후 다시 stk 에 넣는다
            if len(stk) >= 2 : # 연산자가 있을 때 stk의 숫자가 2개보다 적으면 연산이 불가하다
                if ch == '+' : stk.append(stk.pop()+stk.pop())
                elif ch == '*' : stk.append(stk.pop()*stk.pop())
            else : return 'error'

    if len(stk) > 1 : return 'error' # 모든 연산이 끝났는데 stk 의 길이가 1보다 길면 error
    else: return stk[0] # 아니라면 stk의 첫번째 원소를 반환한다

T = 10
for test_case in range(1,T+1):
    N = int(input()) # equation의 길이
    st = input()

    print(f'#{test_case} {calc(pn(st))}')