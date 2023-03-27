import sys
sys.stdin = open('s_input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split()) # N 개의 피자를 동시에 구울 수 있음, M개의 피자를 화덕에 넣는다
    lst = list(map(int,input().split()))

    # 1 queue에 순서대로 N개를 채운다
    q = []
    for i in range(1,N+1):
        q.append((i,lst.pop(0)))

    # 2 q에서 데이터를 꺼내는 경우 순서대로 append
    while q : # queue 에 원소가 있을 때
        idx, c = q.pop(0) # idx: 피자 번호, c: 치즈의 양
        c = c//2
        if c == 0 : # 만약 치즈가 다 녹았으면
            if lst : # 만약에 더 구워야 할 피자가 남아있으면
                i += 1
                q.append((i,lst.pop(0))) # lst에서 새로운 피자를 가져온다
        else : # 만약 치즈가 아직 남아있으면
            q.append((idx,c)) # 꺼낸 피자를 다시 넣어준다
    # 가장 마지막에 남아있는 피자 번호가 답이다
    ans = idx
    print(f'#{test_case} {ans}')