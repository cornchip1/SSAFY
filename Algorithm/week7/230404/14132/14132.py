import sys
sys.stdin = open('input.txt','r')

dic = {1: 2, 2: 1, 3: 4, 4: 3}
D = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]  # di,dj

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(K)]

    for _ in range(M): # M 번 반복
        for a in range(K):
            i,j,n,d = arr[a][0],arr[a][1],arr[a][2],arr[a][3]
            ni,nj = i+D[d][0],j+D[d][1]

            if ni in (0,N-1) or nj in (0,N-1):
                n = int(n/2)
                d = dic[d]
            arr[a][0], arr[a][1], arr[a][2], arr[a][3] = ni, nj, n, d

        for a in range(K):
            for b in range(a):
                if (arr[a][0],arr[a][1]) == (arr[b][0],arr[b][1]):
                    if arr[a][2] > arr[b][2]:
                        arr[a][2] += arr[b][2]
                        arr[b][2] = 0
                    else:
                        arr[b][2] += arr[a][2]
                        arr[a][2] = 0

    ans = 0
    for lst in arr:
        ans += lst[2]

    print(f'#{tc} {ans}')