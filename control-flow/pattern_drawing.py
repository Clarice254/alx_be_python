# Prompt the user to enter the size of the pattern
rows = int(input("Enter the size of the pattern (positive integer): "))
# Initialize the outer loop counter
i = 1
while i <= rows:
    for j in range(rows):
        print("*" , end=" ")
    print()
    i += 1