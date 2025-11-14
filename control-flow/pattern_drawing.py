pattern_size = int(input("Enter the size of the pattern: "))

i = 0
while i < pattern_size:
    j = 0
    while j < pattern_size:
        print("*", end="")
        j += 1
    print()  # new line after each row
    i += 1

