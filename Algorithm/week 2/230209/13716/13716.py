import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    str1 = [_ for _ in input()]
    str2 = [_ for _ in input()]
    N1,N2 = len(str1),len(str2)

    mx = 0
    cnts = [0]*N1
    for i in range(N1):
        for j in range(N2):
            if str1[i] == str2[j] :
                cnts[i] += 1
        if cnts[i] > mx :
            mx = cnts[i]

    print(f'#{test_case} {mx}')





