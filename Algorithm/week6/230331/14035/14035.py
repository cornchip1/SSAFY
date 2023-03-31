import sys
sys.stdin = open('sample_input.txt','r')

def dfs(i,j,n,tmp):
    global ans, L

    if n == 6 :
        if tmp not in L : L.append(tmp) ; ans += 1
        return

    for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
        ni,nj = i+di,j+dj
        if 0 <= ni < 4 and 0 <= nj < 4 :
            # 1의 자리에 추가하기 위해 이전 값에 10을 곱한다
            dfs(ni,nj,n+1,tmp*10+arr[ni][nj])

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(4)]

    L = []
    ans = 0
    for i in range(4):
        for j in range(4):
            #dfs(i,j,0,[arr[i][j]])
            dfs(i, j, 0, arr[i][j])

    print(f'#{tc} {ans}')