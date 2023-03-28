'''# 10개 중 3개를 고르는 조합
N = 10
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            print(i,j,k)'''

'''# n개에서 r개를 고르는 조합 (재귀)
def nCr(n,r,s) : # s : 선택할 수 있는 구간의 시작
    if r == 0 :
        print(*comb)
    else:
        for i in range(s,n-r+1):
            comb[r-1] = A[i]
            nCr(n,r-1,i+1)

n = 10
r = 3
comb = [0]*3
A = [i for i in range(n)]
nCr(n,r,0)
'''

def f(i,k): # bit[i]를 결정하는 함수 // 0 또는 1
    if i == k : # bit의 모든 원소가 결정됨
        print(*bit) 
    else: 
        bit[i] = 0 # i번 index에 접근했을 때 bit[i] 에 0을 넣는다
        f(i+1,k) # 다음 자리로 이동
        bit[i] = 1 # 다음 자리가 없어서 돌아오면 bit[i]에 1을 넣는다 
        f(i+1,k) # 다음 자리로 이동


A = [7,2,5,3,4]
N = len(A)

bit = [0]*N # bit[i] : A[i] 원소가 부분집합에 표함되는지 표시함

f(0,N)
