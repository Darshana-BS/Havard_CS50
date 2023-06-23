x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

z = round(x + y)

# print(int(z))
# print(float(z))

# round to the nearest integer
# print(round(z))

#separate the digits by commas after every triplet
print(f"{z:,}")

#division
z1 =round(x / y,2)
#print the decimal two digits
print (f"{z1:.2f}")