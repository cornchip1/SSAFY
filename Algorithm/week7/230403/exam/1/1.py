def bin(t,tmp):

    x,y = divmod(t,2) # 몫, 나머지
    if x >= 2: # 몫이 2 이상이면 더 나눌 수 있다
        tmp.insert(0,str(y)) # 맨 앞에 나머지 추가
        bin(x,tmp) # 다시 호출
    else: # 몫이 2 미만이면 더이상 나눌 수 없다
        tmp.insert(0,str(y)) # 나머지부터 맨 앞에 추가
        tmp.insert(0,str(x)) # 맨 앞에 몫 추가

    # 2진수로 변환한 16진수의 자릿수를 4자리로 맞춘다 (4비트)
    if len(tmp) < 4 :
        for _ in range(4-len(tmp)):
            tmp.insert(0,'0')

    tmp = ''.join(tmp)

    return tmp

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 16진수의 길이
    st = input() # 16진수 문자열

    # 알파벳이 포함된 16진수를 10진수로 변환한다
    tmp = []
    for s in st:
        if s.isdigit():
            tmp.append(int(s))
        else:
            tmp.append(ord(s)-ord('A')+10)

    # 10진수를 2진수로 변환하여 ast 에 저장한다
    ast = ''
    for t in tmp :
        ast += bin(t,[])

    ans,cnt = 0,0
    for i in ast :
        if i == '1' : cnt += 1 # 연속한 1의 개수를 더한다
        else:
            ans = max(ans,cnt) # 0을 만나면 cnt 와 ans 중 더 큰 값을 ans로 저장한다
            cnt = 0

    # ast 를 다 순회했다면 cnt 와 ans 중 더 큰값을 ans 로 저장한다
    ans = max(ans,cnt)

    print(f'#{tc} {ans}')