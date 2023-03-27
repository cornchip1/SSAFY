import sys
sys.stdin = open('s_input.txt','r')

def perm(i,k):
    global ans

    if i == k :
        # 순열이 만들어지면
        sm = 0
        for x in range(k):
            # x : 출발점 x +1 : 도착점 좌표 // 각각 1 씩 빼야 index
            sm += arr[p[x]-1][p[x+1]-1]
        if sm < ans: ans = sm; return ans
    else:
        for j in range(1,k):
            if used[j] == 0 :
                p[i] = lst[j]
                used[j] = 1
                perm(i+1,k)
                used[j] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    lst = [n for n in range(1,N+1)] # 방문해야 하는 구역 list

    p = [1] + [0]*(N-1) + [1] # 방문 순서
    used = [1] + [0] * (N-1) # 1은 고정

    ans = 100*N+1

    # 사무실 출발 -> 각 구역 한번씩 방문 -> 사무실 복귀 루트를 확인하기 위한 permutation 함수 호출
    perm(1,N)

    print(f'#{tc} {ans}')