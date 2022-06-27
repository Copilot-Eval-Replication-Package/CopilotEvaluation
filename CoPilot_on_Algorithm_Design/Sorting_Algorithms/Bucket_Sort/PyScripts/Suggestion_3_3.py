

def bucket_sort(array):
    buckets = [[] for _ in range(len(array))]
    for i in range(len(array)):
        buckets[int(len(buckets) * array[i])].append(array[i])
    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])
    return [item for sublist in buckets for item in sublist]"