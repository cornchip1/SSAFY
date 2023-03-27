import sys
sys.stdin = open('s_input.txt','r')

def MAX(lst) :
    mx = 0
    mxidx = 0
    for idx,v in enumerate(lst):
        if mx < v : mxidx, mx = idx,v
    return mxidx,mx
def MIN(lst) :
    mn = 101
    for idx,v in enumerate(lst):
        if mn > v : mnidx,mn = idx,v
    return mnidx,mn

T = 11
for test_case in range(1,T+1):
    N = int(input()) # 덤프 시행 횟수
    lst = list(map(int,input().split()))
    n = 0

    mxidx, mx = MAX(lst)
    mnidx, mn = MIN(lst)

    while n < N :

        lst[mxidx] -= 1
        lst[mnidx] += 1
        mxidx, mx = MAX(lst)
        mnidx, mn = MIN(lst)
        #mx,mn = lst[mxidx],lst[mnidx]
        diff = mx-mn
        if diff <= 1 : break
        n += 1
    print(f'#{test_case} {diff}')