import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(tuple(map(int, input().split())))
    lst.sort(key=lambda x: x[1])  # 종료시각 기준 정렬

    e = lst[0][1]
    ans = 1
    for n in range(1, N):
        if lst[n][0] >= e:
            ans += 1; e = lst[n][1]
        else:
            pass

    print(f'#{tc} {ans}')