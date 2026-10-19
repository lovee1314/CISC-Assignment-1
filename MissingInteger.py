def solution(A):
      # Store distinct values for fast membership checks.
    values = set(A)
    missing = 1


   
    # Find the first positive integer absent from the set
    while missing in values:
        missing += 1


    return missing
