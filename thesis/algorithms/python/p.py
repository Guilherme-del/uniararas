import json
import sys

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main(size='small'):
    with open(f'datasets/{size}/merge_sort.json', 'r') as f:
        arr = json.load(f)
    sorted_arr = merge_sort(arr)
    print(f'Sorted {size} dataset with {len(arr)} elements.')

if __name__ == '__main__':
    size = sys.argv[1] if len(sys.argv) > 1 else 'small'
    main(size)
