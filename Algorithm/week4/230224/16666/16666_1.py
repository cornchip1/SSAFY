import sys
sys.stdin = open('sample_input.txt','r')

'''
N개 중 2개 뽑는 모든 조합
lst = [1,2,3,4,5,6]
i (0 -> N-1)
j (i+1 -> N)

N개 중 3개 뽑는 모든 조합
for i in rnage(0,N-2):
    for j in range(i+1,N-1):
        for j in range(j+1,N): 
.
.
.
'''
T = int(input())
for test_case in range(1,T+1):
    N = input()
    lst = [_ for _ in N]
    alst = [int(N)]
    for i in range(len(N)-1):
        for j in range(i+1,len(N)):
            newlst = []
            lst[i],lst[j] = lst[j],lst[i]
            for x in lst : newlst.append(x)
            if newlst[0] != '0' : alst.append(int(''.join(newlst)))
            lst[i],lst[j] = lst[j],lst[i] # 원상복구

    mx, mn = -1, 1000000000 # 0의 개수가 문제여씀!!!!!
    for n in alst :
        if n < mn : mn = n
        if n > mx : mx = n
    print(f'#{test_case} {mn} {mx} {alst}')
