number_1 = 10
number_2 = 3
try:
    result = number_1 / number_2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")        
finally:
    print("Execution complete.")