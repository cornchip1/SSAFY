import sys
sys.stdin = open('s_input.txt','r')

'''def qsort(lst):
    # [1] 종료조건
    if len(lst) < 2 :
        return lst

    # [2] 단위작업 : p 기준으로 양쪽 정렬
    p = lst[len(lst)-1]
    left, right = [],[]

    for i in range(len(lst)-1):
        if lst[i] < p : # 기준보다 작은 경우 왼쪽에 추가
            left.append(lst[i])
        else: right.append(lst[i])

    # [3] 왼쪽 정렬 결과 + [p] + 오른쪽 정렬 결과
    return qsort(left) + [p] + qsort(right)'''

'''def qsort(lst):
    # [1] 종료조건
    if len(lst) < 2 :
        return lst

    # [2] 단위작업 : p 기준으로 양쪽 정렬
    p = lst.pop() # 가장 오른쪽의 값을 기준으로 삼은 경우
    left, right = [],[]

    for n in lst :
        if n < p : # 기준보다 작은 경우 왼쪽에 추가
            left.append(n)
        else: right.append(n)

    # [3] 왼쪽 정렬 결과 + [p] + 오른쪽 정렬 결과
    return qsort(left) + [p] + qsort(right)'''

# index를 이용하는 방법
def qsort_idx(s,e):
    # [1] 종료조건: 정렬할 개수가 1개 이하인 경우
    if s >= e : return
    # [2] 단위작업 : p 기준으로 정렬
    p,t = e,s
    for i in range(s,e):
        if lst[i] < lst[p]:
            lst[i],lst[t] = lst[t],lst[i]
            t += 1
    lst[t],lst[p] = lst[p],lst[t]
    # [3] t 기준으로 양쪽 정렬 // t 는 이미 정렬됨
    qsort_idx(s,t-1) # 왼쪽
    qsort_idx(t+1,e) # 오른쪽


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    #alst = qsort(lst)
    qsort_idx(0,N-1)

    print(f'#{tc} {lst[N//2]}')