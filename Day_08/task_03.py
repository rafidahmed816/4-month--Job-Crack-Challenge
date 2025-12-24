import time

NUM_OPS = 50_000

# append at end O(1) each time 
lst = []
start = time.perf_counter()
for i in range(NUM_OPS):
    lst.append(i)
end = time.perf_counter()
print(f"append end   : {end - start:.4f} seconds")

#  insert at front O(N) each time
lst = []
start = time.perf_counter()
for i in range(NUM_OPS):
    lst.insert(0, i)
end = time.perf_counter()
print(f"insert front : {end - start:.4f} seconds")