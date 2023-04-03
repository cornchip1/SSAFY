import sys
sys.stdin = open('algo1_sample_in.txt','r')

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    bits = int(input(),16) #  int(value, base) 형식으로 넣으면 밑을 변경할 수 있음

    cnt = ans = 0
    for j in range(0,4*N): # bit0 ~ MSB(최상위 비트) 까지 체크
        if bits&(1<<j): # bit j 가 0이 아닌 경우
            cnt += 1
            ans = max(ans,cnt)
        else:
            cnt = 0

    print(f'#{tc} {ans}')