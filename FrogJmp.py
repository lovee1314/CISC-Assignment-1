def solution(X, Y, D):
    # Calculate the remaining distance.
    distance = Y - X
    jumps = distance // D


    # Add one jump if there is a remaining distance.
    if distance % D != 0:
        jumps += 1


    return jumps
