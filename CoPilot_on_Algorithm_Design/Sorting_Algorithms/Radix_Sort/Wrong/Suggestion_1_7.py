

def sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        less = []
        greater = []
        for num in arr[:-1]:
            if num < pivot:
                less.append(num)
            else:
                greater.append(num)
        return sort(less) + [pivot] + sort(greater)

