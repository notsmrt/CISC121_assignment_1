def solution(A):

    numbers = []
    
    # store unique positive numbers
    for number in A:
        if number > 0 and number not in numbers:
            numbers.append(number)

    missing = 1
    
    # find the first positive number not in the list
    while missing in numbers:
        missing += 1
    return missing
