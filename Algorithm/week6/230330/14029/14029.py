import sys
sys.stdin = open('s_input2.txt','r')

def merge(mleft,mright):
    global cnt 
    l = r = 0
    mlst = []

    if mleft[-1] > mright[-1] : cnt += 1
    while l < len(mleft) and r < len(mright):
        if mleft[l] < mright[r]:
            mlst.append(mleft[l])
            l += 1
        else:
            mlst.append(mright[r])
            r += 1
    while l < len(mleft):
        mlst.append(mleft[l])
        l += 1

    while r < len(mright):
        mlst.append(mright[r])
        r += 1
    return mlst


def msort(lst):

    if len(lst) < 2 : 
        return lst
    
    m = len(lst)//2
    left = lst[:m]
    right = lst[m:]

    mleft = msort(left)
    mright = msort(right)
    return merge(mleft,mright)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    cnt = 0
    ans= msort(lst)[N//2]
    

    print(f'#{tc} {ans} {cnt}')