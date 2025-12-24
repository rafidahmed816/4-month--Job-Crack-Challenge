import time

large_list = list(range(-20000,5000000))

start  = time.perf_counter()
# Search for -5 in the list
if -5 in large_list:
    print("Found -5")
else:
    print("-5 not found.")
    
end = time.perf_counter()
print(f"Execution time: {end - start} seconds")
