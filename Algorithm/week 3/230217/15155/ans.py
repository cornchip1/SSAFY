import sys
sys.stdin = open('s_input (1).txt','r')

# 조건
# 1 'o' 가 5개 연속
# 2 4개 방향으로 뻗어나가면서 ((-1,1),(0,1),(1,1),(1,0)) 1을 확인한다
#   ㄴ 8 방향으로 굳이 확인하지 않아도 된다
# 3 1) 범위를 잘 체크하거나 2) padding 을 해서 범위 error 를 방지한다

def solve(arr) :
    # 가능한 모든 기준 위치를 순회
    for si in range(1,N+1):
        for sj in range(1,N+1):
            # 4 방향으로 뻗어가면서
            for di,dj in ((-1,1),(0,1),(1,1),(1,0)):
                for mul in range(5) :
                    ni, nj = si+(di*mul), sj + (dj*mul)
                    if arr[ni][nj] != 'o' : break
                else : # 모두 'o' 인 경우
                    return 'YES'
    return 'NO'


T = int(input())
for test_case in range(1,T+1) :
    N = int(input()) # NxN 판
    arr = ['.'*(N+2)]+['.'+input()+'.' for _ in range(N)]+['.'*(N+2)]
    ans = solve(arr)
    print(f'#{test_case} {ans}')