import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
papers = [[20,10],[20,20]] # 세로, 가로 길이
for test_case in range(1,T+1):
    N = int(input()) # 20*N 크기의 직사각형
    rec = [20,N] # 세로: 20, 가로: N





    print(f'#{test_case} {rec}')

