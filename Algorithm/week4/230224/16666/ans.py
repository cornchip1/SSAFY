import sys
sys.stdin = open('sample_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    st = list(input())
    N = len(st)
    mn = mx = int(''.join(st))
    for i in range(N-1):
        for j in range(i+1,N):
            st[i],st[j] = st[j],st[i]
            if st[0] != '0' and mx < int(''.join(st)):
                mx = int(''.join(st))
            if st[0] != '0' and mn > int(''.join(st)):
                mn = int(''.join(st))
            st[i],st[j] = st[j],st[i]
    print(f'#{test_case} {mn} {mx}')