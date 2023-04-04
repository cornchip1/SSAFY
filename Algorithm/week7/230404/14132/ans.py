import sys
sys.stdin = open('input.txt','r')

dct = {1: 2, 2: 1, 3: 4, 4: 3}
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]

    # M번 만큼 반복해서 처리
    for _ in range(M):
        # [1] 각 개체 1칸씩 이동 후 경계인 경우 처리
        for i in range(len(arr)):  # arr개수 바뀌므로 len()처리
            # ni      = ci       + di
            arr[i][0] = arr[i][0] + di[arr[i][3]]
            arr[i][1] = arr[i][1] + dj[arr[i][3]]
            if arr[i][0] == 0 or arr[i][0] == N - 1 or arr[i][1] == 0 or arr[i][1] == N - 1:  # 경계인 경우
                arr[i][2] //= 2  # 개수 반으로
                arr[i][3] = dct[arr[i][3]]  # 방향 반대로

        # [2] i, j, n 내림차순 정렬후 같은좌표 합치기
        arr.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
        i = 1
        while i < len(arr):
            if arr[i - 1][:2] == arr[i][:2]:  # 같은좌표면 큰 개수에 합치기
                arr[i - 1][2] += arr[i][2]
                arr.pop(i)
            else:
                i += 1

    ans = 0
    for lst in arr:
        ans += lst[2]
    print(f'#{test_case} {ans}')