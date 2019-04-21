import sys
from array import array

sys.stdin=open('flatten.txt', 'r')

as_int = int
def rearrange(boxes):
    i = 0
    while True:
        if boxes[99-i] < boxes[98-i]:
            temp = boxes[99-i]
            boxes[99-i] = boxes[98-i]
            boxes[98-i] = temp
            i += 1
        else:
            break

    i = 0
    while True:
        if boxes[i] > boxes[1+i]:
            temp = boxes[i]
            boxes[i] = boxes[1+i]
            boxes[1+i] = temp
            i+=1
        else:
            break 

for t in range(1, 11):
    max_dump = as_int(input())
    boxes = sorted(map(as_int, input().rstrip().split(' ')))
    for i in range(max_dump):
        boxes[-1] -= 1
        boxes[0] += 1
        rearrange(boxes)
    print('#%d %d' % (t, boxes[99] - boxes[0]))

    


for i in range(1, 11):
    t = int(input())
    ds = [int(d) for d in input().split()]
    for _ in range(t):
        M = max(ds)
        m = min(ds)
        if M - m <= 1:
            break
        ds[ds.index(M)] -= 1
        ds[ds.index(m)] += 1
    print('#{} {}'.format(i, max(ds) - min(ds)))