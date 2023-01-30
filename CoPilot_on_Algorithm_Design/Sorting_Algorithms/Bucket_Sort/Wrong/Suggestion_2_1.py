

def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        buckets[int(len(arr) * arr[i])].append(arr[i])
    return [x for bucket in buckets for x in bucket]

