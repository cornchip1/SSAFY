import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N,M,K = map(int,input().split()) # N명의 사람 / M 초의 시간동안 K개의 붕어빵
    clst = [0] + list(map(int,input().split()))  # 고객들이 도착하는 시각
    blst = [b*K for b in range(max(clst)//M+2)]
    ans = 'Possible'

    for i in range(1,N+1): # 고객 리스트를 순회하며
        t = clst[i]//M
        if blst[t] > 0 :
            for t1 in range(t,len(blst)):
                blst[t1] -=1
        else: ans = 'Impossible' ; break


    # 교수님 풀이
    # # 1 도착한 사람 수와 만들어진 붕어빵의 개수 비교
    # lst = list(map(int,input().split())) # sort 필요 // 뒤에 온 사람이 앞에 있었을 수도 있기 때문
    # cnt = 0
    # ans = 'Possible'
    # for t in sorted(lst) :
    #     cnt += 1
    #     if cnt > (t//M)*K : ans = 'Impossible' ; break # 도착한 사람 수 > 만들어진 붕어빵의 개수
    #
    # # 2 t 별로 만들어진 붕어빵을 만들어놓고 사람 수와 비교 - 내 풀이

    print(f'#{test_case} {ans}')
