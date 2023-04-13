N,M,CNT = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(CNT)]

dic = {1:2,2:1,3:4,4:3}
di = [0,-1,1,0,0] # -/상/하/우/좌
dj = [0,0,0,1,-1]

sm = 0 # 잡은 상어 크기의 합
if CNT > 0 :
    for sj in range(1,M+1): # 낚시왕은 1초에 한 칸씩 오른쪽으로 이동하며, M+1 칸에 이동하면 멈춘다

        # 상어 잡기
        arr.sort(key = lambda x : (x[1],x[0])) # 열, 행 순대로 sort
        for a in range(len(arr)) :
            if arr[a][1] == sj :
                sm += arr[a][4]
                arr.pop(a)
                break

        # 상어 이동
        # 1 이동
        for lst in arr :

            ci,cj,s,d,z = lst[0],lst[1],lst[2],lst[3],lst[4] # 속력, 방향, 크기

            if d in (1,2): ns = s%((N-1)*2)
            else: ns = s%((M-1)*2)

            while True:
                if 1 <= ci+di[d]*ns < N+1 and 1 <= cj+dj[d]*ns < M+1:
                    ni,nj = ci+di[d]*ns,cj+dj[d]*ns
                    break

                if d == 1 : # 가장 윗줄로 보냄
                    ns -= (ci-1)
                    ci = 1
                elif d == 2 : # 가장 아랫줄로 보냄
                    ns -= (N-ci)
                    ci = N
                elif d == 3: # 가장 오른쪽으로 보냄
                    ns -= (M-cj)
                    cj = M
                elif d == 4: # 가장 왼쪽으로 보냄
                    ns -= (cj-1)
                    cj = 1
                d = dic[d]

            lst[0],lst[1],lst[3] = ni,nj,d

        # 2 합치기
        arr.sort(key = lambda x : (x[0],x[1],x[4]), reverse = True) # 행, 열, 크기 순대로 sort
        n = 1
        while n < len(arr) :
            if (arr[n-1][0],arr[n-1][1]) == (arr[n][0],arr[n][1]): # 좌표가 같으면
                arr.pop(n)
            else: n += 1
print(sm)


# x = 1
# while x <= s :
#     # 방향 전환
#     ni,nj = ci+di[d],cj+dj[d]
#     if ni not in range(1, N+1) or nj not in range(1, M+1):
#         d = dic[d]
#         ni, nj = ci + di[d], cj + dj[d]
#     ci,cj = ni, nj
#     x += 1
#
# lst[0],lst[1],lst[3] = ci,cj,d