import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    for i in range(N):
        for j in range(i,N):
            if lst[i] > lst[j] :
                lst[i],lst[j] = lst[j],lst[i]


    print(f'#{test_case}',*lst)