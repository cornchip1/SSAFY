import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for test_case in range(1,T+1) :
    case = list(map(int,input()))
    ints = list(i for i in range(10))
    temp = [0]*10

    for i in range(len(case)) :
        for j in range(10):
            if case[i] == ints[j] :
                temp[j] += 1

    triplet, run = 0,0
    for k in range(len(temp)):
        if temp[k] >= 3 :
            temp[k] -= 3
            triplet += 1
            print(temp)
            continue
        if temp[k-1] == temp[k]-1 and temp[k+1] == temp[k]+1 :
            run += 1
            print('k', k) #,temp[k-1],temp[k],temp[k+1])
        else :
            print('else')
            continue
    print(triplet,run)


