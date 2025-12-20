x =10 # global scoped
def change_x(x):
    x = 20 # LOCAL SCOPED
    print("Inside function:", x)
change_x(x)
print("Outside function:", x)
