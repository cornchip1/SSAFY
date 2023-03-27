#삼성시의 버스 노선
import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1) :
    N = int(input())
    A,B = [0]*N, [0]*N
    for i in range(N):
        A[i], B[i] = map(int,input().split())
    P = int(input())
    cnts = [0]*P #정류장의 개수만큼 생성
    for j in range(1,P+1):
        Cj = int(input())

    # N개의 버스 노선
    for i in range(N):
        # i 번 버스가 지나가는 정류장 확인
        for x in range(A[i], B[i] + 1):
            # j 번째 정류장을 지나간다면 해당 정류장 +1
            for j in range(1,P+1):
                if j == x :
                    cnts[j-1] += 1

    print(f'#{test_case}', *cnts)