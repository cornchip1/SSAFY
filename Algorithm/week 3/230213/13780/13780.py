import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    case = input()
    stack = []
    result = 1
    for i in case :
        if i == '(' :
            stack.append(i)
        else :
            if stack == [] :
                result = 0
            else : stack.pop()
    if stack != [] :
        result = 0
    print(f'#{test_case} {result}')