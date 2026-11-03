def solution(X, A):

    positions = []
    
    # check each leaf and its time.
    for i in range(len(A)):
        # add position only if not already recorded.
        if A[i] not in positions:
            positions.append(A[i])
        # check if all positions covered.
        if len(positions) == X:
            return i
    return -1
