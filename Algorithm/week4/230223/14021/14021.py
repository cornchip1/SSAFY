import sys
sys.stdin = open('s_input.txt', 'r')


T = int(input())
for test_case in range(1, T + 1):
    N,M,L = map(int,input().split()) # N: 노드의 개수, M: 리프노드의 개수, L :출력
    lst = [0] * (N+1)
    anc = []
    for _ in range(M):
        n, v = map(int,input().split()) # n : 노드 번호, v : 값
        lst[n] = v

    if N % 2 : # 2로 나누어떨어지지 않으면
        for i in range(N,0,-2): # 뒤에서부터 2씩 끊어서
            ni = i // 2 # 부모노드 = 자식 노드의 합
            lst[ni] = lst[i] + lst[i-1]
    else : # 2로 나누어떨어지면
        lst[N//2] = lst[N] # 노드의 개수 // 2 = 부모 노드
        for i in range(N-1,0,-2) :
            ni = i // 2
            lst[ni] = lst[i] + lst[i - 1]

    print(f'#{test_case} {lst[L]}')