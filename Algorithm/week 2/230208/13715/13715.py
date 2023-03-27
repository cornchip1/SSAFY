import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split()) # N : 글자판의 가로, 세로 길이, M : 회문의 길이
    lst = [input() for _ in range(N)]

    # 주석 처리한 내용들은 교수님 설명, 교수님 코드 보면 돌아감
    # # 2) 직접 비교할 때 필요한 함수
    # def isSym(lst, i, M):
    #     for j in range(M//2):
    #         if lst[i+j] != lst[i+M-1-j] :
    #             return False
    #         else :
    #             return True


    for _ in range(2):
        for i in lst:
            for j in range(N-M+1):
                # 1) string slice 로 비교
                if i[j:j+M] == i[j:j+M][::-1]:
                    ans = i[j:j+M]
                # 2) 직접 비교
                # if isSym(lst,i,M):
                #   return = lst[i:i+M]
                    break
                else :
                    continue
        lst = list(zip(*lst))

    # for i in range(N):
    #     for x in range(N-M+1):
    #         if lst[i][x:M+x][::-1] in lst[i] :
    #             ans = lst[i][x:M+x][::-1]
    #             break
    #         else :
    #             pass
    #
    # for j in range(N):
    #     colstr = ''
    #     for i in range(N):
    #         colstr += lst[i][j]
    #     for x in range(N-M+1):
    #         if colstr[x:M+x][::-1] in colstr :
    #             ans = colstr[x:M+x][::-1]
    #             break
    #         else :
    #             pass

    print(f'#{test_case} {"".join(ans)}')