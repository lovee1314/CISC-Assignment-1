def solution(A):
    east = 0
    pairs = 0


    for car in A:
        if car == 0:
            # Count eastbound cars seen so far.
            east += 1
        else:
             # Pair this westbound car with earlier eastbound cars.
            pairs += east


            if pairs > 1_000_000_000:
               return -1
   
    return pairs
