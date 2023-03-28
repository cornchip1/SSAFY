import sys

sys.stdin = open('s_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # [1] 종료시각 기준 오름차순 정렬
    arr.sort(key=lambda x: x[1])
    # arr.sort(key = lambda x : [x[1],x[0]]) # 만약 종료 시각이 같은 경우 앞자리 순서대로 정렬

    # [2] 직전 할당한 작업 종료시각보다 크거나 같은 경우
    last = ans = 0
    for s,e in arr:
        if last <= s : # 할당 가능
            ans += 1
            last = e

    print(f'#{tc} {ans}')