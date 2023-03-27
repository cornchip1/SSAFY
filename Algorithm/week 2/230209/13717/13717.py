import sys
sys.stdin = open('sample_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    A,B = input().split()
    NA,NB = len(A),len(B)
    i,cnt = 0,0

    # while i < NA:
    #     if A[i:i+NB] == B :
    #         cnt += 1
    #         i += NB
    #     else :
    #         cnt += 1
    #         i += 1
    # print(f'#{test_case} {cnt}')

    while i < (NA-NB+1):
        if A[i:i+NB] == B :
            cnt += 1
            i += NB
        else :
            i += 1

    ans = NA+(1-NB)*cnt
    print(f'#{test_case} {ans}')