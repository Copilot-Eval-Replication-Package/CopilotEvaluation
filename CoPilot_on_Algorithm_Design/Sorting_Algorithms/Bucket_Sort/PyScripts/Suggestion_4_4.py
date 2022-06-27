

def bucket_sort(arr):
    # create a bucket for each element in the array
    buckets = [[] for _ in arr]
    # for each element in the array, put it in the bucket
    for i in range(len(arr)):
        buckets[arr[i]].append(arr[i])
    # sort each bucket
    for i in range(len(buckets)):
        buckets[i] = quick_sort(buckets[i])
    # put each bucket's elements back into the array
    arr = []
    for i in range(len(buckets)):
        arr += buckets[i]
    return arr"