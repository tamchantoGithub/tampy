def print_all(*args, **kwargs):
    print("positional:", args)
    print("keyword:", kwargs)

print_all(1, 2, 3, name="Alice", age=30)
# Output:
# Positional: (1, 2, 3)
# keyword: {'name': 'Alice', 'age': 30}