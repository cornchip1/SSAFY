def check(lst):
    vowels = 0
    consonants = 0
    for l in lst:
        if l in ('a','e','i','o','u'): vowels += 1
        else: consonants += 1
    if vowels >= 1 and consonants >= 2 :
        return True

def dfs(n,lst):
    if n == L :
        if check(lst) == True:
            result = ''.join(sorted(lst))
            if result not in alst:
                alst.append(result)
        return

    for i in range(C):
        if len(lst) >= 1 :
            if ord(strlst[i]) > ord(lst[-1]) and v[i] == 0 :
                v[i] = 1
                dfs(n+1,lst + [strlst[i]])
                v[i] = 0
        else:
            if v[i] == 0 :
                v[i] = 1
                dfs(n + 1, lst + [strlst[i]])
                v[i] = 0

L,C = map(int,input().split())
strlst = sorted(list(input().split()))
alst = []
v = [0]*C
dfs(0,[])

for a in alst:
    print(''.join(a))