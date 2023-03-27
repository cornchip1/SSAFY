import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input()))

    #빈도수 배열에 빈도 표시
    cnts = [0] * 10
    for n in lst :
        cnts[n] += 1

    #전체를 순회하며 최대값의 index 찾기 (같은 개수면 큰 값을 반환해라)
    idx = 0
    for i in range(1,10) :
        if cnts[idx] <= cnts[i] :
            idx = i

    print(f'{test_case} {idx} {cnts[idx]}')