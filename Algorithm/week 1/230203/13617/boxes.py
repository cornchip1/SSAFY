import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for test_case in range(1,T+1) :
    N,Q = map(int,input().split()) #N: 5, Q:2
    boxes = [0]*N
    for i in range(1,Q+1): #1,2
        L,R = map(int,input().split()) #1,3/2,4
        for j in range(L-1,R):
            boxes[j] = i

    print(f'#{test_case}', *boxes)