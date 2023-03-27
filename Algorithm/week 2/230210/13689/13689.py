import sys
sys.stdin = open('input.txt','r')

def check(word):
    n = len(word)
    result = False

    for i in range(n):
        if word[i] != word[-(i+1)] :
            break
    else :
        result = True
    return result

T = 10
for test_case in range(1,T+1):
    _ = int(input()) # tc
    N = 100
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        word = ''
        for j1 in range(N-1):
            for j2 in range(j1+1,N):
                word = arr[i][j1:j2]
        print(word)



    print(f'#{test_case} {check(word)}')