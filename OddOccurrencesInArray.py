def solution(A):
    result = 0


    # Cancel matching pairs using XOR.
    for value in A:
        result ^= value


    # Return the unpaired value.
    return result
