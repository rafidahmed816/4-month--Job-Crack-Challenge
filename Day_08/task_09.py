items = [("key1", "val1"), ("key2", "val2"), ("key3", "val3")]

# Building the dict: O(N)
my_dict = {k: v for k, v in items}

# Searching the dict: O(1)
result = my_dict.get("key2")