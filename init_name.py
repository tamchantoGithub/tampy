def greet():
    print("Hello, from my_module!")

greet()

print(__name__)
if __name__ == "__init_name__":
    greet()