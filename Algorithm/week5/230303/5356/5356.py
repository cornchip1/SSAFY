import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = 5
    arr = [input() for _ in range(5)]

    st = ''
    for j in range(15):
        for i in range(5):
            if j < len(arr[i]) :
                st += arr[i][j]

    print(f'#{test_case} {st}')