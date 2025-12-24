
large_list = list(range(1000000))

import time

start = time.perf_counter()
list_length = len(large_list)
end = time.perf_counter()
print(f"List length: {list_length}")
print(f"Execution time: {end - start} seconds")