import sys
sys.stdin = open('input.txt','r')

# 후위표기식으로 변환
def preord(n):
    global eqlst
    if n :
        preord(ch1[n])
        preord(ch2[n])
        eqlst.append(lst[n])
    return eqlst

def cal(eq):
    stk = []
    for i in eq:
        if i.isdigit() : stk.append(int(i))
        else:
            if len(stk) >= 2:
                if i == '+' : stk.append(stk.pop(-2) + stk.pop(-1))
                elif i == '-' : stk.append(stk.pop(-2) - stk.pop(-1))
                elif i == '*': stk.append(stk.pop(-2) * stk.pop(-1))
                elif i == '/':
                    try : stk.append(stk.pop(-2) / stk.pop(-1))
                    except ZeroDivisionError : return 'error'
            else: stk.append(i)
    return stk

T = 10
for test_case in range(1,T+1):
    N = int(input()) # 정점의 총 개수
    lst = [0]*(N+1)
    ch1 = [0] * (N+1); ch2 = [0]*(N+1)
    for i in range(1,N+1):
        data = input().split()
        lst[i] = data[1]
        if data[1].isdigit() == 0 : ch1[i] = int(data[2]) ; ch2[i] = int(data[3])

    eqlst = []
    preord(1)
    ans = cal(eqlst)[0]
    print(f'#{test_case} {int(ans)}')