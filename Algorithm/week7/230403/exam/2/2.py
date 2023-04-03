import sys
sys.stdin = open('algo2_sample_in.txt','r')

def dfs(n,s,sm,path): # 방문한 곳의 수 / start point / 배터리 사용량 / 방문 순서
    global ans

    # 가지치기 : sm 이 ans 보다 크면 정답 갱신 가능성이 없다
    if sm > ans : return

    # 종료 조건
    if n == N : # 방문한 곳의 수가 최대 방문 개수에 도달하면 중단한다
        sm += arr[s][0] # 다시 사무국으로 복귀할 때 에너지 소비량을 더한다
        if sm < ans : ans = sm
        return

    # 단위 호출
    for i in range(1,N): # 사무국은 이미 방문함, 1 ~ N-1 의 강의실
        if v[i] == 0 : # 방문하지않은 강의실이면
            if i in (a,b): # i 강의실이 a, b 중에 있다면
                '''
                조건: 두 강의실 a, b 는 반드시 a를 먼저 들른 후 b를 방문해야 한다고 한다.
                즉, a 강의실을 방문하기 전에 b 강의실을 이미 들렀거나, b 강의실을 방문했을 때 a 강의실이 미방문 상태이면 안된다
                '''
                if i == a and v[b] == 0 or i == b and v[a] == 1:
                    # a 강의실에 왔을 때 b 강의실이 미방문 상태이거나, b 강의실에 왔을 때 a 강의실이 방문 상태이면 가능함
                    v[i] = 1 # 방문 처리
                    dfs(n+1,i,sm+arr[s][i],path+[i]) # 방문 횟수 + 1 / i 강의실을신규 start point로 / 배터리 사용량 갱신
                    v[i] = 0 # 미방문 처리
            else: # i 강의실이 a, b 중에 없다면 이하 동일
                v[i] = 1
                dfs(n + 1,i,sm + arr[s][i],path + [i])
                v[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    a,b = map(int,input().split())

    v = [0] * N
    ans = 100 * N + 1

    dfs(1,0,0,[0])

    print(f'#{tc} {ans}')