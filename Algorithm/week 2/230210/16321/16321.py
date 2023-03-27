import sys
sys.stdin = open('sample_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # N x N 격자판
    plane = [input() for _ in range(N)]
    ans = 'yes'

    si,sj,ei,ej = N,N,0,0

    for i in range(N):
        for j in range(N):
            if plane[i][j] == '#':
                if si > i :
                    si = i
                if sj > j :
                    sj = j
                if ei < i :
                    ei = i
                if ei < j :
                    ej = j

    if (ei - si) != (ej - sj) :
        ans = 'no'
    else :
        for i in range(si,ei+1):
            for j in range(sj,ej+1):
                if plane[i][j] != '#':
                    ans = 'no'
                    break
            if ans == 'no':
                break

    print(f'#{test_case} {ans}')
