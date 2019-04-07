class N:
    maxp = 0
    tr = 0
class L:
    n = 0
l = [None] * 1000000
for i in range(1, int(input())+1):
    N.maxp = 0
    N.tr = 0
    L.n = int(input())
    for j, p in enumerate((int(e) for e in input().split(' '))):
        l[j] = p
    for k in range(L.n-1, -1, -1):
        if l[k] > N.maxp:
            N.maxp = l[k]
        else:
            N.tr += N.maxp - l[k]
    print('#{} {}'.format(i, N.tr))
