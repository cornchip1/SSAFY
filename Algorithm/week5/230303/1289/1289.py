import sys
sys.stdin = open('input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    st = input()
    ans = 0
    if st[0] == '1' : ans += 1 # 맨 앞이 1이면 무조건 한번 바꿔야 함
    for i in range(1,len(st)):
        if st[i-1] != st[i]: ans += 1 # 내 앞의 자리와 다르다면 바꿔야 함
    print(f'#{test_case} {ans}')