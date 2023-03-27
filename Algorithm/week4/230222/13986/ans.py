import sys
sys.stdin = open('s_input.txt','r')

# def postord(S):
#     global ans
#     if S :
#         postord(ch1[S])
#         postord(ch2[S])
#         ans += 1

# # 재귀 return / 정답에는 {postord(n)} 만 넣어도 됨
# def postord(n):
#     if n :
#         return postord(ch1[n]) + postord(ch2[n])+1
#     return 0

T = int(input())
for test_case in range(1,T+1):
    E, S = map(int,input().split()) # E: 간선의 개수 S: root(시작점)
    lst = list(map(int,input().split()))

    # 1 트리 저장
    ch1 = [0] * (E + 2);
    ch2 = [0] * (E + 2)

    for i in range(0,len(lst),2):
        p,c = lst[i],lst[i+1]
        if ch1[p] == 0 : ch1[p] = c
        else: ch2[p] = c

    # 2 필요한 인자 생성
    ans = 0
    postord(S) # 기준 위치부터 순회 (노드 : + 1)

    print(f'#{test_case} {ans}')