import sys
sys.stdin = open('input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # 알파벳과 숫자 쌍의 개수
    string = ''
    for _ in range(N) :
        letter, num = input().split()
        string += letter*int(num)

    print(f'#{test_case}')
    for i in range(0,len(string),10):
        print(string[i:i+10])
