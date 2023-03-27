import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    # P : 전체 페이지 수, A : A가 찾아야 하는 페이지, B : B가 찾아야 하는 페이지
    P, A, B = map(int,input().split())
    l, r = 1, P

    def trial(l,r,x) :
        start = l
        end = r
        cnt = 0
        while start <= end :
            centre = int((start+end)/2)
            if centre == x :
                cnt += 1
                return cnt
                break
            elif centre < x :
                 cnt += 1
                 start = centre
            elif centre > x :
                cnt += 1
                end = centre
            return -1 # 디버깅을 위해, 만약 말도 안되는 값이 나오면 바로 인지 가능
    def winner(a,b) :
        if a < b :
            result = 'A'
        elif a > b :
            result = 'B'
        elif a == b :
            result = 0
        return result

    print(f'#{test_case} {winner(trial(l,r,A),trial(l,r,B))}')
