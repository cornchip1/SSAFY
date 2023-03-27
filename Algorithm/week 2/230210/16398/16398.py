import sys
sys.stdin = open('input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # 알파벳 종류 개수

    # 압축을 해제한 전체 문자열 만들기
    ans = ''
    for _ in range(N):
        letter, cnt = input().split()
        ans += letter * int(cnt)

    # 10개씩 출력
    print(f'#{test_case}')
    for i in range(0, len(ans), 10):
        print(ans[i:i+10])





