import sys
sys.stdin = open('input.txt','r')
T = 11
for test_case in range(1,T+1):
    _ = input()
    q = list(map(int,input().split()))

    # n = 1
    # while True : # 무한루프를 사용하고 break 를 넣는 것이 더 쉽다!
    #     t = q.pop(0)-n
    #     if t < 0 : t = 0 # t = max(0,t)
    #     q.append(t)
    #     if t == 0 : break
    #     n = n%5+1

    n = t = 1
    while t :
        t = q.pop(0) - n
        if t < 0: t = 0  # t = max(0,t)
        q.append(t)
        n = n % 5 + 1

    print(f'#{test_case}', *q)