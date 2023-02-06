

def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]
    for i in arr:
        buckets[int(i * len(arr))].append(i)
    for i in range(len(buckets)):
        buckets[i] = quick_sort(buckets[i])
    return [i for bucket in buckets for i in bucket]