import sys
sys.stdin = open('input.txt','r')

def postord(n):
    if tree[n] : # 노드가 존재한다면
        if tree[n] == '+' : return postord(ch1[n]) + postord(ch2[n])
        elif tree[n] == '-' : return postord(ch1[n]) - postord(ch2[n])
        elif tree[n] == '*' : return postord(ch1[n]) * postord(ch2[n])
        elif tree[n] == '/' : return postord(ch2[n]) // postord(ch2[n]) # inter 로 반환해야 하므로 / 가 아니라 //
        else : return int(tree[n]) # 연산자가 아닌 문자열 숫자인 경우 숫자로 바꿔서 반환
    else : return 0 # 존재하지 않으면 0 반환 (이 문제에서는 발생하는 경우가 없음)

T = 10
for test_case in range(1,T+1):
    N = int(input()) # 정점의 총 개수
    tree, ch1, ch2 = [[0]*(N+1) for _ in range(3)] # 오호!
    # 1 완전 이진트리가 아닐 수 있으므로 ch1, ch2 를 만들어서 tree를 담는다
    for _ in range(N):
        tlst = input().split()
        idx = int(tlst[0]) # 노드 번호
        tree[idx] = tlst[1] # 연산자 또는 숫자(str)
        if len(tlst) > 2 : ch1[idx], ch2[idx] = int(tlst[2]), int(tlst[3])

    # 2 순회 (계산식이므로 후위순회)
    ans = postord(1) # 루트부터 (여기서는 루트가 1)

    print(f'#{test_case} {ans}')