import sys
sys.stdin = open('s_input.txt','r')

'''
저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.
N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과, 
N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.
'''
# 완전이진트리, inorder 사용하는 tree structure

def inord(n):
    global cnt
    if 1 <= n <= N :
        inord(n*2) # left child node로 접근
        lst[n] = cnt; cnt += 1 # assign cnt to root
        inord(n*2+1) # right child node로 접근

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    lst = [0] * (N+1)
    cnt = 1
    inord(1) # root 부터 숫자 저장
    print(f'#{test_case} {lst[1]} {lst[N//2]}')