arr = [1, 3, 5]
def sum(arr):
    #if(len(arr) == 1):
    #    return arr[0]
    #return arr.pop(len(arr) - 1) + sum(arr)
    if (arr==[]):
        return 0
    return arr[0] + sum(arr[1:])

print sum(arr)
