import sys
sys.stdin = open('input.txt','r')

priority = {'+':1,'*':2}

def pn(eq) : # 후위표기식으로 변환
    stk = []
    lst = []
    for i in eq :
        if i.isdigit() : lst.append(i) # 피연산자일 때 lst에 넣는다
        else : # 연산자일 때
            while stk and priority[stk[-1]] >= priority[i]: # 연산자가 stk의 top 연산자보다 우선순위가 높아질때까지
                lst.append(stk.pop()) # stk 의 연산자를 빼낸다
            stk.append(i) # stk에 연산자를 넣는다

    while stk : lst.append(stk.pop()) # 스택에 남아있는 연산자를 모두 출력한다
    return lst

def cal(pneq): # 후위표기식 계산
    stk = []

    for i in pneq :
        if i.isdigit(): stk.append(int(i)) # 피연산자일 때 int 로 변환하여 stk 에 넣는다
        else:
            if stk: # stk이 비어있지 않다면
                if i == '+' : stk.append(stk.pop()+stk.pop()) # 연산자가 + 면 원소를 두개 빼서 더하고 다시 넣는다
                if i == '*' : stk.append(stk.pop()*stk.pop()) # * 면 원소를 두개 빼서 곱하고 다시 넣는다
    if stk :
        if len(stk) > 2 : return 'error' # 길이가 2보다 길면 error
        ans = stk[0] # 답은 stk의 원소 (1개일 것)

    return ans

T = 10
for test_case in range(1,T+1):
    _ = int(input()) # 테스트 케이스 길이
    eq = input() # 테스트 케이스

    print(f'#{test_case} {cal(pn(eq))}')
