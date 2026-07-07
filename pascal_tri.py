n = int(input("Enter the number of rows: "))

for i in range(n):
    number = 1

    # Print spaces
    for j in range(n - i - 1):
        print(" ", end=" ")

    # Print Pascal numbers
    for j in range(i + 1):
        print(number, end=" ")
        number = number * (i - j) // (j + 1)

    print()