import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    # 다음의 개수를 공백으로 구분하여 출력
    # 점이 완전히 직사각형 내부에 있음 / 점이 직사각형의 네 변 중 적어도 하나의 위에 있음 / 점이 완전히 직사각형 외부에 있음
    X1,Y1,X2,Y2 = map(int,input().split())
    N = int(input())
    cnts = [0] * 3

    for _ in range(N):
        x,y = map(int,input().split())
        # 점이 완전히 직사각형 내부에 있는 경우
        if X1 < x < X2  and Y1 < y < Y2 : cnts[0] += 1
        # 점이 직사각형의 네 변 중 적어도 하나의 위에 있음
        elif (x == X1 and Y1 <= y <= Y2) or (x == X2 and Y1 <= y <= Y2) or (y == Y1 and X1 <= x <= X2) or (y == Y2 and X1 <= x <= X2): cnts[1] += 1
        # 점이 직사각형 외부에 있음
        else : cnts[2] += 1

    print(f'#{test_case}', *cnts)