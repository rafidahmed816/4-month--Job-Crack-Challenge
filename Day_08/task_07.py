list_a = list(range(10000))
list_b = list(range(5000, 15000))

# O(N^2) 
duplicates = []
for x in list_a:
    for y in list_b:
        if x == y:
            duplicates.append(x)

# O(N) using sets
set_b = set(list_b)
optimized_duplicates = [x for x in list_a if x in set_b]