import time

NUM_OPS = 50_000

#  pop from end (O(1))
lst = list(range(NUM_OPS))
start = time.perf_counter()
for _ in range(NUM_OPS):
    lst.pop()
end = time.perf_counter()
print(f"pop end      : {end - start:.4f} seconds")

#  pop from front (O(N) each time)
lst = list(range(NUM_OPS))
start = time.perf_counter()
for _ in range(NUM_OPS):
    lst.pop(0)
end = time.perf_counter()
print(f"pop front    : {end - start:.4f} seconds")
