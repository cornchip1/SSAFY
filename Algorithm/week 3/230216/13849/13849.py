import sys
sys.stdin = open('s_input.txt','r')

# def dfs(i,j,sm) :



T = int(input())
for test_case in range(1,T+1) :
    N = int(input()) # NxN 배열
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되게 한다
    js = []

    for i in range(N):
        mn = 0
        for j in range(N-1) :
            if arr[i][j] < arr[i][j+1] :
                mn = j
                if mn not in js: js.append(mn)
            elif arr[i][j] > arr[i][j+1] :
                mn = j+1
                if mn not in js : js.append(mn)
    sm = 0
    for idx, value in enumerate(js) :
        sm += arr[idx][value]


    print(f'#{test_case} {sm}')
