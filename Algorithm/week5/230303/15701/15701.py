import sys
sys.stdin = open('input.txt','r')

T = 10
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        t = []
        for j in range(N):
            if arr[j][i] != 0 : t.append(arr[j][i])
        # 교착 상태에 남아있는 자석을 제외하고 없애기
        s,e = 0,-1
        while t[s] != 1 :
            t.pop(0)
        while t[e] != 2 :
            t.pop()


        temp = []
        for c in t :
            if temp:
                if c == 1 : temp.append(c)
                else: temp.clear()
            else:
                if c == 1 : temp.append(c); cnt += 1

    print(f'#{test_case} {cnt}')

