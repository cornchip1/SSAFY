# 1953
import sys
sys.stdin = open('sample_input.txt','r')

pipe = [[],[0,1,2,3],[0,1],[2,3],[0,3],[1,3],[2,1],[2,0]] # 파이프로 갈 수 있는 방향
di,dj = [(-1,0),(1,0),(0,-1),(0,1)] # 상/하/좌/우




T = int(input())
for test_case in range(1,T+1):
    N,M,R,C,L = map(int,input().split()) # NxM / start point = arr[R][C] / L : time
    arr = [list(map(int,input().split())) for _ in range(N)]



    print(f'#{test_case}')
