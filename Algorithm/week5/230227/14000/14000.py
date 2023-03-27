import sys
sys.stdin = open('s_input.txt', 'r')

dic = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
def solve(arr):
    for st in arr :
        if '1' in st: # 1이 있는 경우 처리
            # 1 끝부터 처음 1을 만나는 지점 찾기 : e
            for e in range(len(st)-1,-1,-1):
                if st[e] == '1': break
            # 2 7자리씩 숫자로 변환
            pwd = []
            for i in range(e-55,e+1,7):
                pwd.append(dic[st[i:i+7]])

            # 3 검증
            if (sum(pwd[0:8:2])*3 + sum(pwd[1:8:2])) % 10 == 0 :
                return sum(pwd[0:8:2])+sum(pwd[1:8:2])
            return 0

T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())

    arr = [input() for _ in range(N)]
    N, M = len(arr), len(arr[0])

    ans = solve(arr)
    print(f'#{test_case} {ans}')
