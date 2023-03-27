import sys
sys.stdin = open('s_input.txt','r')
T = 10
for t in range(1,T+1) :
    tc = int(input())
    # 사다리 불러오기
    arr = [list(map(int,input().split())) for _ in range(100)]
    # 도착 지점 찾기
    si, sj = 99, 0 # 마지막 행 탐색, 열은 모르기 때문에 0으로 우선 설정
    for j in range(100):
        if arr[si][j] == 2 :
            sj = j

    # 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하므로
    # 도착지점에서 거꾸로 올라올 때는 좌/우/위 순서로 이동 가능한 곳이 있는지 탐색
    di = [0, 0, -1]
    dj = [-1, +1, 0]

    # 도착지점에서 타고 올라오기, si = 0이 될 때까지
    while si > 0 :
        # 좌/우/위 차례로 시도
        for n in range(3) :
            ni = si + di[n]
            nj = sj + dj[n]
            # ni, nj 가 사다라 범위 내에 있는지 확인
            if 0 <= ni < 100 and 0 <= nj < 100 :
                # 새로운 위치의 값이 1인지 확인, 아니라면 이동하지 않음
                if arr[ni][nj] == 1 :
                    # si, sj에 새로운 값을 지정해준다
                    si, sj = ni, nj
                    # 한 자리에서 계속 머물지 않도록 지나온 자리는 값을 바꿔준다
                    arr[ni][nj] = 3
                    break
                else :
                    continue

    print(f'#{tc} {sj}')































    # arr = [list(map(int,input().split())) for _ in range(100)]
    #
    # # move ladder up, right, left
    # di = [0,0,-1]
    # dj = [+1,-1,0]
    #
    # # find the goal point and start from there
    # # arr[99][gp]
    # si, sj = 99, 0
    # for j in range(100) :
    #     if arr[si][j] == 2 :
    #         sj = j
    #
    # while si > 0:
    #     for n in range(3) :
    #         ni = si + di[n]
    #         nj = sj + dj[n]
    #         if 0 <= nj < 100 and 0 <= ni < 100:
    #             if arr[ni][nj] == 1 :
    #                 arr[ni][nj] = 0
    #                 si,sj = ni,nj
    #                 break
    #
    # print(f'#{test_case} {sj}')