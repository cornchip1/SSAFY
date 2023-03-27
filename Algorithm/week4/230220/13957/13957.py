import sys
sys.stdin = open('input.txt','r')
T = 10
for test_case in range(1,T+1):
    _ = input()
    nlst = list(map(int,input().split()))

    while True :
        if nlst[-1] == 0 : break
        else:
            for x in nlst :
                for i in range(1,6):
                    if nlst[0]-i <= 0 :
                        nlst.pop(0)
                        nlst.append(0)
                        break
                    else: nlst.append(nlst.pop(0)-i)
                break

    print(f'#{test_case}', *nlst)