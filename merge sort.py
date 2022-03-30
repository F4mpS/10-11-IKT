# a = [4, 22, 55, 99, 111, 162, 211, 444]
# b = [3, 11, 13, 66]
#
#
def merge(a, b):
    c = []
    while a and b:
        if a[0] <= b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    return c + a + b


A = [45, 531, 33, 3, 1, 5, 7]


def mergeSort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    L = mergeSort(A[:mid])
    R = mergeSort(A[mid:])
    return merge(L, R)


C = mergeSort(A)

print(C)
