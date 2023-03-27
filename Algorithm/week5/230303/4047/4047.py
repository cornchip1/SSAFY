import sys
sys.stdin = open('sample_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    st = input()
    N = len(st)

    lst = []
    ans = [13]*4 #SDHC
    for c in range(0,N,3):
        info = st[c:c+3]
        if info not in lst :
            lst.append(info)
            if info[0] == 'S' : ans[0] -= 1
            elif info[0] == 'D' : ans[1] -= 1
            elif info[0] == 'H' : ans[2] -= 1
            elif info[0] == 'C' : ans [3] -= 1
        else: ans = 'ERROR' ; break

    if ans == 'ERROR':
        print(f'#{test_case} {ans}')
    else:
        print(f'#{test_case}',*ans)