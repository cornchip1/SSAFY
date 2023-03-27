import sys
sys.stdin = open('input.txt','r')
T = 10
for test_case in range(1,T+1):
    N = int(input()) # 찾아야 하는 회문의 길이
    plane = [input() for _ in range(8)]

    # 가로 또는 세로로 이어진 회문의 개수만 센다
    # 직선으로만 이어져야 한다

    di = [+1,0]
    dj = [0,+1]

    check = []
    for i in range(8) :
        for j in range(8):
            for k in range(2):
                txt = []
                for n in range(N):
                    ni = i + di[k]*n
                    nj = j + dj[k]*n
                    if 0 <= ni < 8 and 0 <= nj < 8 :
                        txt.append(plane[ni][nj])
                if len(txt) == N :
                    check.append(txt)
    palindrome = []
    for c in check :
        for x in range(1,(N//2)+1):
            if c[x-1] != c[-x]:
                break
        else :
            palindrome.append(c)

    cnt = len(palindrome)
    print(f'#{test_case} {cnt}')