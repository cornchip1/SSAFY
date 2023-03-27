import sys
sys.stdin = open('s_input.txt','r')
T = 10
for test_case in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    i,mn,mnidx,mx,mxidx = N,101,0,0,0

    while i > 0 :
        for idx, height in enumerate(lst[1:]):
            if height > mx :
                mx = height
                mxidx = idx
            if height < mn :
                mn = height
                mnidx = idx
        if lst[mxidx] - lst[mnidx] <= 1 :
            break
        else :
            lst[mxidx] -= 1
            lst[mnidx] += 1
            mx, mn = mx-1, mn+1
        i -= 1

    print(lst[mxidx],lst[mnidx],mx-mn)