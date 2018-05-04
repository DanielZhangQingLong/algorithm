def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i> pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print quicksort([3, 12, -3, 32, 5, 55, 9, 78, -18])

    
