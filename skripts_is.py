smallest = None
print("Before")
for value in [3,31,12,9,74,15]:
    if smallest is None :
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)
