import helpers

numbers = [1, 2, 3]
for num in numbers:
    # find TARGET
    if num == 5:
        print("Found 5!")
        break
    else:
        print(f"5 was not found. IT'S {num}.") # output: 5 was not found.
