import sys
sys.stdin = open('s_input.txt','r')
check = ['{','}','(',')']
result = 1
T = int(input())
for test_case in range(1,T+1):
    string = input()
    temp = []
    result = 1

    # 괄호만 골라내기
    for i in string :
        if i in check :
            temp.append(i)
        else : pass


    stack = []
    for i in temp :
        if i == '{' or i  == '(':
            stack.append(i)
        else :
            if stack == []:
                result = 0
            else :
                if i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                else :
                    result = 0
    if stack != [] :
        result = 0

    print(f'#{test_case} {result}')

