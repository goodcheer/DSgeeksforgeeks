class N:
    mode = 0
    key = ''
s = {str(i): 0 for i in range(0, 101)}

for i in range(1, int(input())+1):
    for k in s.keys():
        s[k] = 0
    N.mode = 0
    input()
    for e in input().split():
        s[e] += 1
    for k, v in s.items():
        if v > N.mode:
            N.mode = v
            N.key = k
        elif (v == N.mode) and (k > N.key):
            N.key = k
    print('#{} {}'.format(i, N.key))
