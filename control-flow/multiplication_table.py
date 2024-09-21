#Ask the user to input a number for which they want to see the multiplication table
number = float(input("Enter a number to see its multiplication table: "))
#Generate multiple table
for x in range(1,11):
    product = number * x
    print(f"{number} * {x} = {product}")