import sys
sys.stdin = open('input1.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    num = input()
    cnts, ans = 0,0

    for i in num :
        if i == '1':
            cnts += 1
        else :
            cnts = 0
        if cnts > ans :
            ans = cnts

    print(f'#{test_case} {ans}')