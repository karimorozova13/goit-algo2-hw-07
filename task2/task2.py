from functools import lru_cache
import matplotlib.pyplot as plt
import timeit

from tree import SplayTree

@lru_cache(maxsize=10)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n-1) + fibonacci_lru(n-2)
    
def fibonacci_splay(n, tree):
    if n < 2:
        return n
    
    cached_value = tree.find(n)
    if cached_value is not None:
        return cached_value
    
    result = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, result)
    return result

nums = [i for i in range(0, 950 + 1, 50)]
tree = SplayTree()

lru_times = []
splay_times = []

print(f"{'n':<10} | LRU Cache Time (s) | Splay Tree Time (s)")
print("-" * 55)
for n in nums:
    lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=3) / 3
    splay_time = timeit.timeit(lambda: fibonacci_splay(n, tree), number=3) / 3

    lru_times.append(lru_time)
    splay_times.append(splay_time)
    print(f"{n:<15}{lru_time:<20.8f}{splay_time:<20.8f}")

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(nums, lru_times, label="LRU Cache", marker="o")
plt.plot(nums, splay_times, label="Splay Tree", marker="s")
plt.xlabel("Число Фібоначчі (n)")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння часу виконання для LRU Cache та Splay Tree")
plt.legend()
plt.grid()
plt.show()
