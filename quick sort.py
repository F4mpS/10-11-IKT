import random


def qSort(A):
    if len(A) <= 1:
        return A
    x = random.choice(A)

    bl = [b for b in A if b < x]
    bx = [b for b in A if b == x]
    br = [b for b in A if b > x]
    return qSort(bl) + bx + qSort(br)


arr = [515, 53,-3, 11, 22, 22, 22, 22, 55, 11]

print(qSort(arr))
