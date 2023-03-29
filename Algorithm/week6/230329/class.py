'''# merge sort basic
def merge(left,right):
    pass

T = int(input())

def msort(m):
    if len(m) == 1 :
        return m

    middle = len(m)//2
    left = m[0:middle]
    right = m[middle:]

    left = msort(left)
    right = msort(right)
    return merge(left,right)
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    msort(arr)'''

# merge sort completed
'''def msort(s,e):
    if s == e : # 즉, 분할할 원소가 하나만 남으면
        return
    m = (s+e)//2
    msort(s,m) # 왼쪽 절반 분할
    msort(m+1,e) # 오른쪽 절반 분할

    # merge
    k = 0
    l, r = s, m+1 # 왼쪽과 오른쪽에서 가장 작은 숫자의 위치
    while l <= m or r <= e :
        if l <= m and r <= e : # 둘 다 내부에 머물고 있으면
            if arr[l] <= arr[r] :
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1
        elif l <= m : # l 은 남아있고 r 은 벗어난 상태
            while l <= m :
                tmp[k] = arr[l]
                l += 1
                k += 1
        elif r <= e : # r은 남아있고 l은 벗어난 상태
            while r <= e :
                tmp[k] = arr[r]
                k += 1
                r += 1
    i = 0
    while  i < k :
        arr[s+i] = tmp[i] # 임시로 합친 것을 원래의 자리에 넣기
        i += 1

    return
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    tmp = [0]*N
    msort(0,N-1)
    print(arr)'''


# quick sort : Hoare partition

def hoare(A,l,r) :
    pivot = A[l] # 맨 왼쪽원소를 기준으로 함
    i,j = l,r # l : pivot 보다 큰 값을 찾아 오른쪽으로 이동, r : pivot 보다 작은 값을 찾아 왼쪽으로 이동
    while i <= j :
        while i <= j and A[i] <= pivot : # 멈추는 조건 : 1) i,j 가 교차 2) pivot 보다 큰 원소를 만남
            i += 1 # 아니라면 하나씩 증가
        while i <= j and A[j] >= pivot : #  # 멈추는 조건 : 1) i,j 가 교차 2) pivot 보다 작은 원소를 만남
            j -= 1
        if i < j : # 교차되지 않은 상태에서 멈췄다면
            A[i],A[j] = A[j],A[i] # 두 원소의 위치 교환
    # 교차해서 멈췄다면
    A[j],A[l] = A[l],A[j]
    return j # pivot은 j에 위치한다

def qsort(A,l,r):
    global cnt
    cnt += 1
    if l < r : # 실존하는 구간일 때 // 오른쪽 끝이 실제로 오른쪽에 있을 때
        s = hoare(A,l,r)
        qsort(A,l,s-1)
        qsort(A,s+1,r)


T = int(input())
for tc in range(1,T+1):
    cnt = 0

    N = int(input())
    arr = list(map(int,input().split()))
    tmp = [0]*N
    qsort(arr,0,N-1)
    print(*arr, cnt)