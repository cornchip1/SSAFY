import sys
sys.stdin = open('s_input.txt','r')

def perm(i,k):
    global ans

    if i == k :
        if p[0] == p[1] == p[2] : # triplet
            if p[3] == p[4] == p[5] or (p[3] == p[4] + 1 and p[4] == p[5] + 1) or (p[3] + 1 == p[4] and p[4] + 1 == p[5]) :
                ans = 1
        elif (p[0] == p[1] + 1 and p[1] == p[2] + 1) or (p[0] + 1 == p[1] and p[1] + 1 == p[2]): # run
            if p[3] == p[4] == p[5] or (p[3] == p[4] + 1 and p[4] == p[5] + 1) or (p[3] + 1 == p[4] and p[4] + 1 == p[5]) :
                ans = 1
    else:
        for j in range(k):
            if used[j] == 0 :
                p[i] = lst[j]
                used[j] = 1
                perm(i+1,k)
                used[j] = 0
    return ans

T = int(input())
for tc in range(1,T+1):
    lst = [int(_) for _ in input()]
    p, used = [0]*len(lst), [0]*len(lst)
    ans = 0
    perm(0,len(lst))

    print(f'#{tc} {ans}')