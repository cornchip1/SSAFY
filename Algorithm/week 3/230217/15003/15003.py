import sys
sys.stdin = open('s_input (1).txt','r')
T = int(input())
for test_case in range(1,T+1):
    data = [ int(_) for _ in input()]
    N = len(data)
    initial = [0]*N
    ans = 0 # 수정 횟수

    for i in range(N) :
        if data[i] != initial[i]: # i 번째 값이 같지 않으면
            ans += 1 # 수정 횟수 +1
            if data[i]  == 1 : # i의 자리에서 원본 데이터가 1이면 그 뒤는 다 1로 변환
                for n in range(i,N):
                    initial[n] = 1
            else : # i의 자리에서 원본 데이터가 1이 아니면 (즉 0 이면) 그 뒤는 다 1로 변환
                for n in range(i,N) :
                    initial[n] = 0

    print(f'#{test_case} {ans}')
