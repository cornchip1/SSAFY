'''
selection sort 를 전체를 돌리면 비효율적
어차피 10개의 숫자들만 반환하고,
홀수 index에는 작은 순서대로, 짝수 index 에는 큰 순서대로 넣으므로
홀수/짝수 구분하여 selection sort 를 진행한다
'''

import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input().split()))

    # selection sort를 부분적으로만 (10개) 진행
    for i in range(10):
        idx = i
        for j in range(i+1,N) :
            if i % 2 == 0 :
                if lst[idx] < lst[j] :
                    idx = j
            else :
                if lst[idx] > lst[j] :
                    idx = j
        lst[i],lst[idx] = lst[idx],lst[i]
    print(f'#{test_case}', *lst[:10])