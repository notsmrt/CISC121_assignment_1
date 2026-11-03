def solution(A, K):
    n= len(A)

    if n == 0:
        return A
    # rotate the array K times.
    for i in range(K):
        # store last element.
        last = A[-1]
        # shift all elements 1 index right
        for j in range(n - 1, 0, -1):
            A[j] = A[j - 1]
        # move the stored last element to the front.
        A[0] = last
    return A
