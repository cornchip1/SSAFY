def solution(s):
    answer = []
    binary, zero = 0, 0  # 이진 변환의 횟수, 제거된 모든 0의 개수

    q = []
    q.append(s)

    while q:
        string = q.pop(0)
        if string == '1': break

        # 1 s의 모든 0 떼기
        tmp = ''
        for i in string:
            if i == '0':
                zero += 1  # 제거된 0의 개수 +1
            else:
                tmp += i

        # 2 이진 변환
        c = len(tmp)
        b = []

        def bin(c):
            x, y = divmod(c, 2)  # 몫, 나머지
            if x > 1:
                b.insert(0, str(y))
                return bin(x)
            else:
                if x == 1 :
                    b.insert(0, str(y))
                    b.insert(0, str(x))
                else:
                    b.insert(0,str(y))
            return ''.join(b)

        q.append(bin(c))
        binary += 1

    answer = [binary, zero]
    return answer
