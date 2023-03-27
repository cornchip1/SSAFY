import sys
sys.stdin = open('s_input.txt', 'r')

# 풀이
# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
# 1) dictionary 만들기 - 효율적으로 만드는 방법
# 2) counts 만들어서
# 3) 출력식 만들기

dic = {}
strn = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for x in range(len(strn)):
    dic[strn[x]] = x

T = int(input())
for test_case in range(1, T + 1):
    tc, N = input().split()
    lst = input().split()
    cnts = [0] * 10

    for i in lst :
        for n in range(10) :
            if dic[i] == n :
                cnts[n] += 1

    ans = ''
    for i in range(10):
        ans += (strn[i]+' ') * cnts[i]
    print(f'{tc}\n{ans[:-1]}')

    # ans = ' '.join(lst)
    # print(f'{tc} {ans}')