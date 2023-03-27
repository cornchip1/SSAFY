import sys
sys.stdin = open('s_input.txt','r')

def QSORT(lst):
    # 종료 조건
    if len(lst) <= 1 : return lst

    # 단위 작업
    pivot = lst.pop()
    l, r = [],[]
    for i in lst :
        if i < pivot : l.append(i)
        else: r.append(i)
    return QSORT(l) + [pivot] + QSORT(r)

T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # 정수의 개수
    nlst = list(map(int,input().split())) # 정수 리스트
    alst = QSORT(nlst)
    print(f'#{test_case} {alst[N//2]}')