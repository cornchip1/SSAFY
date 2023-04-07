import sys
sys.stdin = open('input.txt','r')

dic = {1:2,2:1,3:4,4:3}
di, dj = [0,-1,1,0,0],[0,0,0,-1,1]

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(K)]

    for _ in range(M):
        for a in range(len(arr)):
            i,j,cnt,d = arr[a][0],arr[a][1],arr[a][2],arr[a][3]
            ni,nj = i+di[d],j+dj[d]
            if ni in (0,N-1) or nj in (0,N-1):
                cnt //= 2
                d = dic[d]
            arr[a][0],arr[a][1],arr[a][2],arr[a][3] = ni,nj,cnt,d

        arr.sort(key = lambda x : (x[0],x[1],x[2]), reverse= True)

        n = 1
        while n < len(arr):
            if (arr[n-1][0],arr[n-1][1]) == (arr[n][0],arr[n][1]):
                arr[n-1][2] += arr[n][2]
                arr.pop(n)
            else: n += 1

    ans = 0
    for lst in arr:
        ans += lst[2]

    print(f'#{tc} {ans}')