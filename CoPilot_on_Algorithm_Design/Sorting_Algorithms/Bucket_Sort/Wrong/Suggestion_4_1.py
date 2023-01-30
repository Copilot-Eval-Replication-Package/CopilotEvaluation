

def bucket_sort(arr):
    # create a bucket for each element in the array
    buckets = [[] for _ in range(len(arr))]
    # put each element in the bucket
    for i in range(len(arr)):
        buckets[i].append(arr[i])
    # sort each bucket
    for bucket in buckets:
        bucket.sort()
    # put each bucket back into the array
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            arr[i] = buckets[i][j]
    return arr

