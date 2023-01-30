

def bucket_sort(array):
    buckets = [[] for _ in range(len(array))]
    for i in range(len(array)):
        buckets[int(len(array) * array[i])].append(array[i])
    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])
    return [x for bucket in buckets for x in bucket]

