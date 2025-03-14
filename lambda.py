
def add(x,y):
    return  x+y
print(add(1,2))

# can't use LAMBDA in this case
# print(lambda x,y: x+y)

# but you can use LAMBDA in this case
print((lambda x,y: x+y) (1, 2) )  # Output: 3