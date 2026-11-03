def solution(A):

    n = len(A)
    # store unique elements
    numbers = set(A)

    # check for duplicates
    if len(numbers) != n:
        return 0
    # make sure every number from 1 to n exists.
    for number in range(1, n + 1):
        if number not in numbers:
            return 0
    return 1
