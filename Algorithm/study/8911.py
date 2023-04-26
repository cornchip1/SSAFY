direction = [(1,0),(0,-1),(-1,0),(0,1)]
T = int(input())
for tc in range(1,T+1):
    movement = input()

    i,j = 0,0
    d = 0
    top, bottom, left, right = 0,0,0,0

    for m in movement:
        if m == 'L':
            if d == 3 : d = 0
            else: d += 1
        elif m == 'R':
            if d == 0 : d = 3
            else: d -= 1
        elif m == 'F':
            i,j = i + direction[d][0], j + direction[d][1]
        elif m == 'B':
            i,j = i - direction[d][0], j - direction[d][1]

        top, bottom, left, right = max(top,i), min(bottom,i), min(left,j), max(right,j)


    area = (top-bottom) * (right-left)

    print(area)
