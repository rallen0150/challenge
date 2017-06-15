arr = [4, 1, -16, 3.14, 5]
# min = -16, 1
# max = 4, 5
n=2

def min_max(arr, n):
    return sorted(arr)[:n][-n:] #Or this way
    # arr = sorted(arr)
    # min_value = arr[:n]
    # max_value = arr[-n:]
    # return min_value, max_value

print(min_max(arr, n))
