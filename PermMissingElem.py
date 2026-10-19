def solution(A):
    n = len(A)


    # Calculate the sum of integers from 1 to n + 1.
    expected = (n + 1) * (n + 2) // 2


    # Subtract the actual sum to find the missing value.
    return expected - sum(A)
