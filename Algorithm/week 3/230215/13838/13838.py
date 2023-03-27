import sys
sys.stdin = open('s_input.txt','r')

priority = {'*': 3, '+': 2}
T = int(input())

for test_case in range(1,T+1):
    expr = input() # 중위표기식

    stk = []
    ans = ''

    for i in expr :
        if i in priority.keys(): # 연산자인 경우
            if stk != [] : # stk 이 비어있지 않은 경우
                if priority[i] > priority[stk[-1]] : # 연산자의 우선순위가 stk 의 top 의 우선순위보다 높은 경우
                    stk.append(i) # 연산자를 stk에 넣는다
                else : # 연산자의 우선순위가 stk 의 top 의 우선순위보다 낮은 경우
                    while stk and priority[i] <= priority[stk[-1]]: # top의 연산자의 우선순위가 연산자의 우선순위보다 작거나 같을 때까지 stk에서 빼낸다
                        ans += stk.pop()
                    stk.append(i)  # 그 다음 연산자를 push 한다
            else : # stk 이 비어있는 경우
                stk.append(i)
        else : # 연산자가 아닌 경우
            ans += i

    while stk :
        ans += stk.pop()


    print(f'#{test_case} {ans}')

    #1 952*+1+33*7*6*+
    #2 443*4*9*+2+74*7*+77*9*5*2*+88*+
    #3 23+99*+8+21*+32*3*1*+33*+1+2+36*2*7*4*+9+

    #1 952*+1+33*7*6*+
    #2 443*4*9*+2+74*7*+77*9*5*2*+88*+
    #3 23+99*+8+21*+32*3*1*+33*+1+2+36*2*7*4*+9+
