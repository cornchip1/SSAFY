def solution(arr):
    answer = arr[0]

    # 유클리드 호제: 최대공약수 구하기
    def euclid(a, b):
        a,b = max(a, b),min(a, b)

        while (a % b) != 0:
            r = a % b
            a = b
            b = r
        return b

    # 최소공배수 = 두 수의 곱 / 최대공약수
    for i in range(1, len(arr)):
        gcd = euclid(answer, arr[i])
        lcm = answer * arr[i] // gcd
        answer = lcm

    return answer

print(solution([2,6,8,14]))