# O(N^2) approach 
s = ""
for i in range(10000):
    s += "a"

# O(N) approach
chars = []
for i in range(10000):
    chars.append("a")
optimized_s = "".join(chars)