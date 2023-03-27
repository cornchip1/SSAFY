import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    cards = input() # 6장의 카드의 숫자
    lst = [int(i) for i in cards] # 리스트로 변형
    run, triplet, result = 0, 0, 0

    nums = [i for i in range(10)]
    cnts = [0]*10

    for i in lst:
        for n in range(10) :
            if i == nums[n] :
                cnts[n] += 1

    for n in range(10) :
        if cnts[n] >= 3 :
            cnts[n] -= 3
            triplet += 1
    for x in range(8):
        if cnts[x] >= 1 and cnts[x+1] >= 1 and cnts[x+2] >= 1 :
            cnts[x] -= 1
            cnts[x+1] -= 1
            cnts[x+2] -= 1
            run += 1
    if run + triplet == 2 :
        result = 1

    print(f'#{test_case} {result}')

