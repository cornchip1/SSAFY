import sys
sys.stdin = open('s_input.txt','r')

#number of test cases
T = int(input())

#number of elements in list
for test_case in range(1,T+1) :
    N = int(input())
    boxes = list(map(int,input().split()))

    ans = 0
    for i in range(N-1) :
        cnt = 0
        for j in range(i+1,N):
            if boxes[i] > boxes[j] :
                cnt += 1
        if ans < cnt :
            ans = cnt

    print(f'#{test_case} {ans}')