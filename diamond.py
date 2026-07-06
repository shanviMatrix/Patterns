n = int(input("Enter the number of rows: "))

# Upper Pyramid
for i in range(n):
    # Spaces
    for j in range(n - i - 1):
        print(" ", end=" ")

    # Stars
    for j in range(2 * i + 1):
        print("*", end=" ")

    print()

# Lower Inverted Pyramid
for i in range(1, n):
    # Spaces
    for j in range(i):
        print(" ", end=" ")

    # Stars
    for j in range(2 * (n - i) - 1):
        print("*", end=" ")

    print()