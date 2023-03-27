import sys
sys.stdin = open('input.txt','r')

def preord(n) :
    if n : # 존재하는 노드라면 처리
        alst.append(n) # 방문: 필요한 처리
        preord(ch1[n]) # 왼쪽노드 먼저
        preord(ch2[n]) # 그다음 오른쪽노드

    #return

T = int(input())
for test_case in range(1,T+1):
    V = int(input()) # 정점의 총 개수
    lst = list(map(int,input().split()))

    # 1 트리 구조 저장
    # 완전 이진트리가 아니므로 left, right 자식 노드를 저장할 lst 생성
    ch1 = [0]*(V+1)
    ch2 = [0] * (V+1)

    for i in range(0,len(lst),2):
        p,c = lst[i],lst[i+1]
        if ch1[p] == 0 : ch1[p] = c
        else: ch2[p] = c

    # 2 트리 순회
    alst = []
    preord(1) # 루트 = 1 (given)

    print(f'#{test_case}',*alst)