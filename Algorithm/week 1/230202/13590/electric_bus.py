import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1) :
    K,N,M = map(int,input().split())
    lst = list(map(int,input().split())) + [N]
    s = 0
    cnt = 0
    for i in range(M):
        if s + K == lst[i] :
            cnt += 1
            s = lst[i]
        elif s+K > lst[i]:
            if s+K < lst[i+1] :
                cnt += 1
                s = lst[i]
            else : pass
        else : # s + K < lst[i]
            cnt = 0
            break
    print(f'#{test_case} {cnt}')
