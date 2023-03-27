import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1) :
    lst = list(map(int,input()))
    ans = 0

    #find frequency of each integers
    cnts = [0] * 10
    for n in lst :
        cnts[n] += 1

    #find triplets
    i = 0
    while i <= 9 :
        #if triplet exists, add 1 to ans, remove 3 equal numbers
        if cnts[i] >= 3 :
            ans += 1
            cnts[i] -= 3
        else :
            i += 1

    #find runs
    i = 0
    while i <= 7 :
        if cnts[i] >= 1 and cnts[i+1] >= 1 and cnts[i+2] >= 1 :
            ans += 1
            cnts[i] -= 1
            cnts[i+1] -= 1
            cnts[i+2] -= 1
        else :
            i += 1

    print(f'#{test_case} {ans//2}')