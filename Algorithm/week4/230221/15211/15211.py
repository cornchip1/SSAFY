import sys
sys.stdin = open('input.txt','r')

def BFS(si,sj,ei,ej) :
    # 필요한 요소 생성
    v = [[0]*16 for _ in range(16)]
    q = []
    # q enqueue, 방문처리
    q.append((si,sj))
    v[si][sj] += 1

    # q 가 비어있지 않으면
    while q :
        ci,cj = q.pop(0)
        # 정답 처리
        if (ci,cj) == (ei,ej) : return 1
        # 반복 작업 - 상/하/좌/우 이동
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            # 범위 내에 있고 벽이 아니라면
            if 0 <= ni < 16 and 0 <= nj < 16 and arr[ni][nj] != 1:
                q.append((ni,nj)) # q에 넣는다
                arr[ni][nj] = 1 # 지나온 길 표시
                v[ni][nj] = v[ci][cj] + 1 # 몇번째로 방문했는지 표시

    # q가 바닥났는데도 도착지점까지 가지 못한다면 0 반환
    return 0



T = 10
for test_case in range(1,T+1):
    _ = input()
    arr = [list(int(_) for _ in input()) for _ in range(16)]

    si,sj,ei,ej = 0,0,0,0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2 : si,sj = i,j ; break
            if arr[i][j] == 3 : ei,ej = i,j ; break

    print(f'#{test_case} {BFS(si,sj,ei,ej)}')