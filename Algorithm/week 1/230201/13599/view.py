import sys
sys.stdin = open('s_input.txt','r')

T = 3
for test_case in range(1,T+1):
    N = int(input()) #테스트 케이스의 길이
    buildings = list(map(int,input().split()))

    sm = 0
    #check buildings
    for i in range(2,N-2): #ignore first and last two
        min_r = 255
        result = 0
        for j in (-2,-1,1,2):
            if (buildings[i] - buildings[i+j]) > 0 :
                result = buildings[i] - buildings[i+j]
                print(result)
                if result < min_r :
                    min_r = result
        sm += min_r
        print(i,min_r, sm)
        #sum minimum values
        #if min_r != 1000000:
        #    sm += min_r

    # check = [-2,-1,1,2]
    # sm = 0
    #
    # #check buildings
    # for i in range(2,N-2): #ignore first and last two
    #     result = [0]*len(check)
    #     for j in range(len(check)) :
    #         if (buildings[i] - buildings[i+check[j]]) > 0 :
    #             result[j] = buildings[i] - buildings[i+check[j]]
    #
    #     #sort result list
    #     min_r = result[0] #assume the first element of result list is the minumum value
    #     for x in range(1,len(result)):
    #             if result[x] < min_r :
    #                 min_r = result[x]
    #     #sum minimum values
    #     sm += min_r

    print(f'#{test_case} {sm}')