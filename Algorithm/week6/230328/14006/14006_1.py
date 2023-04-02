import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]

    lst.sort(key= lambda x : x[1])

    ans = 1
    e = lst[0][1]
    for i in range(1,N):
        if lst[i][0] >= e :
            ans += 1
            e = lst[i][1]


    print(f'#{tc} {ans}')