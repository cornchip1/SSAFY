import sys
sys.stdin = open('sample_input.txt','r')

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

    mx = mn = int(N)
    for n in alst :
        if n < mn : mn = n
        if n > mx : mx = n
    print(f'#{test_case} {mn} {mx} {alst}')