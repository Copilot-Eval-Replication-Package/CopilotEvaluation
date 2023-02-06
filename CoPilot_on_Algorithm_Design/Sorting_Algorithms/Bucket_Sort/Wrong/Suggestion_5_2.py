def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        buckets[i].append(arr[i])
    return [min(bucket) for bucket in buckets]
