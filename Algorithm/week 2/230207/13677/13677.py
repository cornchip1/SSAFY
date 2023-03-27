import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # 리스트의 길이
    lst = list(map(int,input().split()))

    # 선택 정렬
    def selectionSort(lst,N):
        for i in range(N-1):
            minidx = i
            for j in range(i+1,N) :
                if lst[minidx] > lst[j] :
                    minidx = j
            lst[i],lst[minidx] = lst[minidx],lst[i]
        return lst

    lst = selectionSort(lst,N)
    new_lst = [0]*10

    x = 0
    while x < 10 :
        if x % 2 == 0 :
            new_lst[x] = lst[-1]
            lst = lst[:-1]
        else :
            new_lst[x] = lst[0]
            lst = lst[1:]
        x += 1

    print(f'#{test_case}', *new_lst)