import sys
sys.stdin = open('input.txt','r',encoding = 'UTF8')
T = 10
for _ in range(T):
    tc = input()
    key = input()
    strs = input()

    N, n = len(strs),len(key)
    cnt = 0

    for i in range(N-n):
        if strs[i:i+n] == key:
            cnt += 1

    print(f'#{tc} {cnt}')
