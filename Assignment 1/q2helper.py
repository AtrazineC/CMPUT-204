def PutInPlace(A, j, x):
    print(A)
    if j == 0:
        A[0] = x
    elif x > A[j - 1]:
        A[j] = x
    else:
        A[j] = A[j - 1]
        PutInPlace(A, j - 1, x)
    print(A)

def InsertionSort(A, n):
    if n > 1:
        print(A)
        InsertionSort(A, n - 1)
        x = A[n - 1]
        print(A)
        PutInPlace(A, n - 1, x)
        print(A)

if __name__ == '__main__':
    A = [4, 7, 2, 8, 6, 5]
    n = 6
    InsertionSort(A, n)
    print(A)
