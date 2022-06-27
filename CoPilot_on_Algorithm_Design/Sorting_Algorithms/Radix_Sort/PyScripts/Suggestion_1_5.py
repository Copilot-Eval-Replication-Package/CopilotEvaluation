

def radix_sort(array):
    max_digit = 0
    for i in array:
        if len(str(i)) > max_digit:
            max_digit = len(str(i))
    for i in range(1, max_digit+1):
        buckets = [[] for _ in range(10)]
        for j in array:
            buckets[(j//10**(i-1))%10].append(j)
        array = []
        for k in buckets:
            array.extend(k)
    return array

