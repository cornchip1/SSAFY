import sys
sys.stdin = open('sample_input.txt','r')

def dfs_ter(n2,tmp2,flag):
    if n2 == N2 or flag == 1:
        if tmp2 != ter:
            sm = 0
            for j in range(1,N2+1):
                if tmp2[-j]:
                    sm += int(tmp2[-j]) * 3**(j-1)
            s2.append(sm)
        return

    if not v2 :
        v2.append(n2)
        for i in range(1,3):
            tmp2[n2] = (tmp2[n2]+i)%3
            dfs_ter(n2+1,tmp2,1)
            tmp2[n2] = (tmp2[n2]-i)%3
        v2.pop()
        dfs_ter(n2+1,tmp2,0)


def dfs_bin(n1,tmp1,flag):
    if n1 == N1 or flag == 1:
        if tmp1 != bin:
            sm = 0
            for i in range(1,N1+1):
                if tmp1[-i] == 1:
                    sm += 2**(i-1)
            # print(tmp1,sm)
            s1.append(sm)
        return
    if not v1 :
        v1.append(n1)
        tmp1[n1] = (tmp1[n1]+1)%2
        dfs_bin(n1 + 1, tmp1, 1)
        v1.pop()
        tmp1[n1] = (tmp1[n1]-1) % 2
        dfs_bin(n1+1,tmp1,0)


T = int(input())
for tc in range(1,T+1):
    bin,ter = [int(_i) for _i in input()], [int(_j) for _j in input()]

    N1,N2 = len(bin),len(ter)
    tmp1, tmp2 = bin[:], ter[:]
    v1, v2 = [],[]
    s1,s2 = [],[]

    dfs_bin(0,tmp1,0)
    dfs_ter(0,tmp2,0)

    ans = 0
    for b in s1:
        if b in s2: ans = b

    print(f'#{tc} {ans}')