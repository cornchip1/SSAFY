import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N = 5
    words = [input() for _ in range(N)]

    # 배열의 크기 구하기
    for _i in range(N):
        M = 0
        if M < len(words[_i]) : M = len(words[_i])

    # arr로 옮겨넣기 (빈 자리는 공백으로)
    arr = [['']*M for _ in range(N)]
    for i in range(N):
        for j in range(len(words[i])):
            arr[i][j] = words[i][j]

    # 세로로 읽기
    ans = ''
    for i in range(M):
        for j in range(N):
            ans += arr[j][i]

    print(f'#{test_case} {ans}')