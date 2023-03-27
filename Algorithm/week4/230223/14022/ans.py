import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # 노드의 개수
    lst = list(map(int, input().split()))

    # 1 힙 데이터 저장
    h = [0] * (N + 1)
    last = 0

    for n in lst :
        last += 1
        h[last] = n # 가장 끝 위치에 데이터 삽입
        # 부모노드가 있고, 나보다 크면 교환
        c = last
        while 0 < c//2 and h[c//2] > h[c] :
            h[c//2], h[c] = h[c],h[c//2]
            c = c//2

    # 2 last부터 조상노드(들)의 합을 저장
    ans = 0
    c = last//2
    while c : # c가 존재하는 조상인 경우
        ans += h[c]
        c//=2 # 부모 노드로 이동

    print(f'#{test_case} {ans}')