import sys
sys.stdin = open('s_input.txt','r')

cal = ['+','-','*','/']

def Forth(expr):

    stk = []
    v = [0]*len(expr)
    ans = 0

    for i in range(len(expr)) :
        if expr[i] in cal : # 연산자이면
            if len(stk) >= 2 : # stk 에 숫자가 2개 이상 있으면 연산이 가능하다
                v[i] = 1
                n2 = stk.pop()
                n1 = stk.pop()
                # 숫자 두개를 뽑아서 연산을 수행하고 다시 stk 에 넣는다
                if expr[i] == '+' : stk.append(n1+n2)
                if expr[i] == '-' : stk.append(n1-n2)
                if expr[i] == '*' : stk.append(n1*n2)
                if expr[i] == '/' : stk.append(int(n1/n2)) # 또는 n1//n2
            else : # 연산자를 만났을 때 stk 에 숫자가 2개 미만이면 연산이 불가하다
                return 'error'
        elif expr[i] == '.' : # '.' 이면 stk 에서 숫자를 꺼내 출력한다
            if len(stk) > 1 :
                return 'error'
            else :
                v[i] = 1
                for x in range(len(expr)):
                    if v[x] != 1 :
                        return 'error'
                        break
                else:
                    ans = stk.pop()
        elif '.' not in expr :
            return 'error'
        else : # 연산자가 아니면 stk에 넣는다
            v[i] = 1
            stk.append(int(expr[i]))
    if len(stk) > 1 :
        return 'error'
    return ans # 연산이 잘 되었으면 stk 의 값은 하나일 것이다

T = int(input())
for test_case in range(1,T+1):
    expr = list(input().split())

    print(f'#{test_case} {Forth(expr)}')


