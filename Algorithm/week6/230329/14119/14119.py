import sys
sys.stdin = open('sample_input (3).txt','r')

T = int(input())
for tc in range(1,T+1):
    charge = list(map(int,input().split())) # 1일 / 1개월 / 3개월 / 1년 요금
    plan = list(map(int,input().split())) # 연간 이용 계획 / 월별 기일 수
    

    ans = 3000*31+1

    print(f'#{tc} {ans}')