R,C,M = map(int,input().split())


sharks = dict()
res = 0

for _ in range(R):
    # 위치/속력/방향/크기
    # 위치 : key / 나머지 : values
    r,c,s,d,z = map(int,input().split())
    sharks[(r,c)] = [s,d,z]

    # 방향 : 1 2 3 4 -> 상/하/우/좌
    fisherman = -1
    while fisherman < C :
        # 1 낚시왕 이동
        fisherman += 1

        # 2 가장 가까운 상어 잡기
        for i in range(R):
            if (i,fisherman) in sharks :
                shark = sharks[(i,fisherman)]
                res = shark[2]
                del shark

        # 3 상어의 이동
        next_sharks = {} # 다음에 상어들이 이동할 좌표를 한번에 구하기
        for key, value in sharks.items():
            x,y = key # 나, 상어, (r, c)
            s, d, z = value # 속력, 방향, 크기

            for _ in range(s): # 방향에 따라 이동
                # 방향이 위/아래이면 s = s%(세로*2-2)
                if d in (1, 2):
                    s = s % (N * 2 - 2)
                else:
                    s = s % (M * 2 - 2)

            while s :
                if d==4:
                    if y > s :
                        y -= s
                        s = 0 # 이동 중단
                    else:
                        y = 0
                        s -= y
                        d = 3
                elif d == 3 :
                    if C - y - 1 > s :
                        y += s
                    else:
                        s = s - (C-y-1)
                        y = C - 1
                        d = 4
                elif d == 2:

                elif d == 1:


        sharks = next_sharks
        # 4 큰 상어가 나머지 상어 먹기
