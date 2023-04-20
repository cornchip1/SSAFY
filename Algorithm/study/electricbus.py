'''
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17
'''

T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))+[N]
    s,ans = 0,0

    for i in range(M):
        if s + K == lst[i]:
            ans += 1; s = lst[i]
        elif s + K > lst[i]:
            if s+K < lst[i+1] :
                ans += 1; s = lst[i]
            else: pass
        else:
            ans = 0 ; break


    print(f'#{tc} {ans}')