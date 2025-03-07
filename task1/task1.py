import time
import random

from lru_cache import LRUCache

def range_sum_no_cache(array, L, R):
    return sum(array[L:R+1])
    
def update_no_cache(array, index, value):
    array[index] = value
    return array[index]

cache = LRUCache(1000)

def range_sum_with_cache(L, R):
    cached_result = cache.get((L, R))
    if cached_result is not None:
        return cached_result
    result = sum(arr[L:R + 1])
    cache.put((L, R), result)
    return result

def update_with_cache(index, value):
    arr[index] = value
    cache.invalidate(index)


N = 100000
Q = 50000
arr = [random.randint(1, 100000) for _ in range(100000)]
queries = [(random.choice(["Range", "Update"]), random.randint(0, N-1), random.randint(0, N-1) if random.choice(["Range", "Update"]) == "Range" else random.randint(1, 100000)) for _ in range(Q)]

def calculate_time(use_cache=False):
    start_time = time.time()
    for query in queries:
        if query[0] == "Range":
            if use_cache:
                range_sum_with_cache(query[1], query[2])
            else:
                range_sum_no_cache(arr, query[1], query[2])
        else:
            if use_cache:
                update_with_cache(query[1], query[2])
            else:
                update_no_cache(arr, query[1], query[2])
    return time.time() - start_time

if __name__ == '__main__':
    time_no_cache = calculate_time()
    time_with_cache = calculate_time(use_cache=True)

    print(f"Час виконання без кешування: {time_no_cache:.2f} секунд")
    print(f"Час виконання з LRU-кешем: {time_with_cache:.2f} секунд")
        