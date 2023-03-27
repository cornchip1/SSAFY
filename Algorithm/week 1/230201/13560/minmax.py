import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for test_case in range(1,T+1) :
    N = int(input()) # 5 <= N <= 1000
    nums = list(map(int,input().split())) #1 <= a <= 100000

    for i in range(N):
        for j in range(i+1,N):
            if nums[i] < nums[j] :
                nums[i],nums[j] = nums[j],nums[i]

    diff = nums[0] - nums[-1]

    print(f'#{test_case} {diff}')