import sys
sys.stdin = open('s_input.txt','r')

def solve(s,e):

    # 1 종료 조건: 더 이상 승부를 보지 않을 때 / 인원이 1명이 되었을 때 승리자의 index return
    if s == e :
        return s

    # 2 단위 작업
    # 2-1 좌/우 그룹에서 각각의 승자 탐색
    a = solve(s,(s+e)//2) # 왼쪽 승자
    b = solve((s+e)//2+1,e) # 오른쪽 승자

    # 2-2 승자 판별
    # if (lst[a]%3) + 1 == lst[b] : return b
    # return a

    # 무법 테이블을 활용한 승자 판별
    tbl = [0,2,3,1]
    if tbl[lst[a]] == lst[b] : return b
    return a

T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # 인원수
    lst = [0] + list(map(int,input().split())) # 카드 번호 - 1: 가위 2: 바위 3: 보
    ans = solve(1,N)
    print(f'#{test_case} {ans}')