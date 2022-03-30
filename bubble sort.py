A = [5, 51, 11, 4, 1]
N = 5

for i in range(N-1):
    for j in range(N-2, i-1, -1):
        if A[j] < A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]


print(A)
