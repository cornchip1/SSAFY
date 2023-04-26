direction = [(-1,0),(0,1),(1,0),(0,-1)]

def check(si,sj):
    result = False
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj = si+di,sj+dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 :
            result = True
    return result

N, M = map(int,input().split()) # 배열의 크기
si, sj, d = map(int,input().split()) # 시작좌표, 방향
arr = [list(map(int,input().split())) for _ in range(N)]

cnt = 0 # 청소하는 칸의 개수

while True:
    if arr[si][sj] == 0 :
        arr[si][sj] = 2; cnt += 1

        # # debug
        # print(f'#{cnt}')
        # for lst in arr:
        #     print(*lst)
    else:
        if check(si,sj) == True:
            while True:
                if d == 0 : d = 3
                else: d -= 1
                ni,nj = si+direction[d][0], sj+direction[d][1]
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 :
                    arr[ni][nj] = 2
                    cnt += 1

                    # # debug
                    # print(f'#{cnt}')
                    # for lst in arr:
                    #     print(*lst)

                    si,sj = ni,nj
                    break
        else:
            ni,nj = si-direction[d][0], sj-direction[d][1]
            if ni < 0 or ni >= N or nj < 0 or nj >= M or arr[ni][nj] == 1:
                break
            si,sj = ni, nj

# for lst in arr:
#     print(*lst)
print(cnt)
