import sys
sys.stdin = open('s_input.txt','r')


num_dic = {'ZRO':0,'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9}
trans_dic = {v:k for k,v in num_dic.items()}

def Ssort(lst) :
    N = len(lst)
    for i in range(N-1):
        minidx = i
        for j in range(i+1,N):
            if lst[minidx] > lst[j] :
                minidx = j
        lst[minidx],lst[i] = lst[i],lst[minidx]
    return lst

T = int(input())
for test_case in range(1,T+1):
    tc, N = input().split()
    N = int(N)
    lst = list(input().split())
    num_lst = [0]*N

    # 숫자로 치환
    for i in range(N):
        num_lst[i] = num_dic[lst[i]]

    # selection sort
    num_lst = Ssort(num_lst)

    # 문자로 변경
    for i in range(N):
        lst[i] = trans_dic[num_lst[i]]

    #ans = f'{tc}\n',*lst
    print(f'{tc}')#\n',*lst)
    print(*lst)
