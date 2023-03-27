import sys
sys.stdin = open('s_input.txt','r')

def qsort(lst):

    # 종료 조건 : 정렬할 요소가 한개일 때
    if len(lst) <= 1 :
        return lst

    # 1 단위 작업 : pivot 을 기준으로 좌, 우로 분리한다
    pivot = lst.pop()
    l,r = [],[]
    for n in lst :
        if n < pivot : l.append(n)
        else : r.append(n) # 같은 값을 가졌어도 어차피 나중에 정리될 것

    # 2 왼쪽 정렬한 결과 + 나 + 오른쪽 정렬 결과
    return qsort(l) + [pivot] + qsort(r)

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    lst = qsort(lst)
    ans = lst[N//2]
    print(f'#{test_case} {ans}')