import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    str1 = input()
    str2 = input()
    result = 0
    if str1 in str2 :
        result = 1
    else :
        pass
    print(f'#{test_case} {result}')