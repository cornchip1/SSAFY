import sys
sys.stdin = open('s_in2.txt','r')

T = int(input())

for test_case in range(1,T+1):
    lst = list(map(int,input().split()))
    N = len(lst)
    ans = 0 # initiate ans as false

    # 공집합을 제외한 모든 조합을 비트로 표시
    for bit in range(1, 1<<N) :
        sm = 0
        # bit의 0의 자리부터 N-1의 자리까지 한 자리씩 확인한다
        for j in range(N) :
            if bit & (1<<j) : #해당 비트가 0 이 아니면
                sm += lst[j]
        if sm == 0 :
            ans = 1
            break

    '''
    for i in range(2) :
        bit[0] = i
        for j in range(2) :
            bit[1] = j
            for k in range(2) :
                bit[2] = k
                for l in range(2) :
                    bit[3] = l
                    for m in range(2) :
                        bit[4] = m
                        for n in range(2) :
                            bit[5] = n
                            for o in range(2) :
                                bit[6] = o
                                for p in range(2) :
                                    bit[7] = p
                                    for q in range(2) :
                                        bit[8] = q
                                        for r in range(2) :
                                            bit[9] = r
                                            s = 0
                                            for x in range(10):
                                                if bit[x] == 1 :
                                                    bit[x] = arr[x]
                                                    s += arr[x]
                                            if s == 0 :
                                                ans = 1
    '''
    print(f'#{test_case} {ans}')