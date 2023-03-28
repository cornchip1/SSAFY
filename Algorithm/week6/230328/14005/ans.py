import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split()) # N개의 컨테이너를 M대의 트럭으로 운반한다
    W = list(map(int,input().split())) # N개의 화물의 무게
    T = list(map(int,input().split())) # M개의 트럭의 적재용량

    # 트럭당 한 개의 컨테이너를 운반할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다
    # 최대 M대의 트럭이 편도로 한번만 운행한다
    # 이동한 화물의 총 중량이 최대 되도록 하는 무게를 구하라
    # 컨테이너를 한개도 옮길 수 없는 경우 0을 출력한다
    ans = 0

    # [1] W, T 모두 내림차순으로 정렬
    W.sort(reverse=True)
    T.sort(reverse=True)

    # [2] 짐을 하나씩 트럭에 싣는다
    i = 0
    for w in W :
        if w <= T[i] : # 현재 대기하고 있는 트럭에 싣을 수 있다
            ans += w
            i += 1
        if i == M : break
    
    print(f'#{tc} {ans}')