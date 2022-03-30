def selectionSort(A, limit):
    # The round of the algorithm
    steps = 0
    # Traverse through all array elements
    for i in range(len(A)-1,-1,-1):
        print(i)
        # Find the minimum element in remaining unsorted array
        max_idx = i
        for j in range(i, -1,-1):
            if A[max_idx] < A[j]:
                max_idx = j
                
        # Swap the found minimum element with the first element        
        A[i], A[max_idx] = A[max_idx], A[i]

        # Increment the current round count
        steps += 1

        # If we hit the steps limit, then return the current list
        if steps == limit:
            return A
    return A
