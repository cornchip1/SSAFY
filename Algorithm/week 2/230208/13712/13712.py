import sys
sys.stdin = open('s_input.txt','r')

def mirror(string):
    string = list(string)
    for x in range(len(string)):
        if string[x] == 'b':
            string[x] = 'd'
        elif string[x] == 'd':
            string[x] = 'b'
        elif string[x] == 'p':
            string[x] = 'q'
        elif string[x] == 'q':
            string[x] = 'p'
    return string

T = int(input())
for test_case in range(1,T+1):
    string = input()
    new = [0]*len(string)

    string = mirror(string)
    for i in range(1,len(string)+1):
        new[i-1] = string[-1*i]
    ans = ''.join(new)

    print(f'#{test_case} {ans}')