import time


large_list = list(range(-20000,5000000))

large_set = set(large_list)
# Search for -5 in the set
start  = time.perf_counter()
if -5 in large_set:
    print("Found -5")
else:
    print("-5 not found.")
    
end = time.perf_counter()
print(f"Execution time: {end - start} seconds")
