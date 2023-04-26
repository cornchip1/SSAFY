from collections import deque
lst = [deque(int(_) for _ in input()) for _ in range(4)]
K = int(input())

for _ in range(K):
    num, d = map(int,input().split())
    # [1] 톱니바퀴 정보 저장
    info = []
    for k in range(4):
        info.append((lst[k][6],lst[k][2]))
    n = num-1

    # [2] 돌리는 톱니바퀴 기준 양 옆으로 돌리는 방향 확인
    # [2-1] 왼쪽 : 맨 왼쪽인 경우 제외
    if n != 0 :
        for l in range(n,0,-1):
            if info[l][0] != info[l-1][1]:
                if (n-l-1)%2: lst[l-1].rotate(-1*d)
                else: lst[l-1].rotate(d)
            else: break

    # [2-2] 오른쪽 : 맨 오른쪽인 경우 제외
    if n != 3 :
        for r in range(n,3):
            if info[r][1] != info[r+1][0]:
                if (r+1-n) % 2 : lst[r+1].rotate(-1*d)
                else: lst[r+1].rotate(d)
            else: break

    # [2-3] 돌려야하는 톱니바퀴 돌리기
    lst[n].rotate(d)

# [3] 점수 계산
score = 1*lst[0][0] + 2*lst[1][0] + 4*lst[2][0] + 8*lst[3][0]
print(score)


