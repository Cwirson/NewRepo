# x = lambda a, b, c: a + b + c
# print(x(5, 10, 5))

# def dbl(n):
#     return lambda a: a * n

# print(dbl(2)(3))  

def false():
    return False

x = "True"
y = True

print(x is y) # jesli 2 zmienne/dane sa takie same /// taki sam obiekt

print(false() is False) # false() oddaje bool i powrownoje z bool
print(false() is True) # False