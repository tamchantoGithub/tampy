x = 10 # Integer
print(type(x)) # Output : <class 'int'>

x = "Hello, Python!" # Now a string
print(type(x))  # Output ; <class 'str'>

def add(a: int, b:int) -> int:
    if type(a) != int:
        print("Invalid: Type a")
    elif type(b) != int:
        print("Invalid: Type b")
    else:
        return a + b
print(add(10, 20))  # 30
print("10", 20) # TypeERROR: CAN ONLY CONCATENATE STR not "int") to str

name = "Alice"
age = 30
print(f"my name is {name} and I am {age} years old.")
# Expressions inside f-strings
print(f"In 5 years, I'll be {age + 5} years old.")