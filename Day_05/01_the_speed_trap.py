#TC O(n)
numbers = list(range(-1000,999000))

print(size := len(numbers))

# create a set
num_set = set(numbers)

# TC: O(1) because of hash table
print(-1 in num_set)  