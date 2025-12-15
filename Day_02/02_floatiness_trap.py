num_1 =0.1
num_2 =0.2
if num_1 + num_2 == 0.3:
    print("The sum is exactly 0.3")
else:
    print(f"The sum is: {num_1 + num_2}")
    
    
# The sum is: 0.30000000000000004    
# Solution: Use round function to limit the precision
if round(num_1 + num_2, 1) == 0.3:
    print("The sum is exactly 0.3")
else:
    print(f"The sum is: {num_1 + num_2}")   