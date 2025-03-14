def mutation(lst):
    lst.append(10)
    return lst

my_numbers = [1, 2, 3]
list_after_call = mutation(my_numbers)

print("my numbers:", my_numbers)
print("Returned list:", list_after_call)