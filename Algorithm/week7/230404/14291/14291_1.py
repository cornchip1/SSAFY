import sys
sys.stdin = open('sample_in.txt','r')

def bfs():

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    bfs()

    print(f'#{tc}')