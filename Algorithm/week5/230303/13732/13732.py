import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#' :
                lst.append((i,j))

    si, sj = lst[0]
    ei, ej = lst[-1]
    ans = 'yes'

    # 가로 세로 길이가 다르면 정사각형이 아니다
    if (ei-si) != (ej-sj) : ans = 'no';
    # 가로 세로 길이가 같으면
    else:
        for ci in range(si,ei+1):
            for cj in range(sj,ej+1):
                # 중간에 # 이 빈 곳이 하나라도 있으면 정사각형이 아니다
                if arr[ci][cj] != '#' : ans = 'no'


    print(f'#{test_case} {ans}')