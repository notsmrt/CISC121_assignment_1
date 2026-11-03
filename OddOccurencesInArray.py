def solution(A):

    counts = {}
    # count occurrence of numbers.
    for number in A:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    # find the number with odd occurrences
    for number in counts:
        if counts[number] % 2 != 0:
            return number
