import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    case = input()
    stack = []

    for i in case :
        if stack != [] and i == stack[-1] :
            stack.pop()
        else :
            stack.append(i)

    ans = len(stack)
    print(f'#{test_case} {ans}')