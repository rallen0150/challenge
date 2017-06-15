arr = [4, 1, -16, 3.14, 5]
# min = -16, 1
# max = 4, 5

def min_max(arr, n):
    return sorted(arr)[:n][-n:]
    # min_value = arr[:n]
    # max_value = arr[-n:]
    # return min_value, max_value
