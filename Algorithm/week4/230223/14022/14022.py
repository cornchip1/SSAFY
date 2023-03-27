import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # 노드의 개수
    data = list(map(int,input().split()))
    h = [0] * (N+1)
    h[1] = data[0]

    # 최소 힙 만들기
    for i in range(2,N+1): # 완전 이진 트리이므로, 첫번째 노드 이후로 두개씩
        # 힙에 자식 노드 값 추가
        h[i] = data[i-1]
        # 부모 노드가 자식 노드보다 큰 경우
        while h[i//2] > h[i]:
            h[i//2],h[i] = h[i],h[i//2] # 두개의 위치 변경
            i = i //2 # 루트 노드로 갈 때까지 검사

    # 마지막 노드의 조상 노드에 저장된 정수의 합 찾기
    sm = 0
    i = N # 마지막 노드
    while i >= 1 : # 루트 노드로 가면서
        i = i//2
        sm += h[i] # 조상 노드들의 값을 더한다

    print(f'#{test_case} {sm}')