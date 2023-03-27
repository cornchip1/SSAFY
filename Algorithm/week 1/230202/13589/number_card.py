import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input()))

    #create list of length 10 to count numbers in lst
    cnts = [0]*10
    for i in lst :
        cnts[i] += 1

    #set initial maximum frequency and most frequent value to 0
    mx = 0
    x = 0

    #get maximum frequency and most frequent value
    for i in range(10):
        #if there are more than one maximum frequency, get the biggest number
        if cnts[i] >= mx and i >= x :
            mx = cnts[i]
            x = i

    print(f'#{test_case} {x} {mx}')