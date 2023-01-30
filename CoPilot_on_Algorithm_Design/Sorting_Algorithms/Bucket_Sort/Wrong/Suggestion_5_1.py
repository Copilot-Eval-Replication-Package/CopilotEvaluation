def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        buckets[int(arr[i] * len(buckets))].append(arr[i])
    return [i for bucket in buckets for i in bucket]

