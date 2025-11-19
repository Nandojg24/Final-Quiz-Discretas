variable1 = 10                                # This is an integer         int()
variable2 = "Hello, World!"                   # This is a string           str()
variable4 = False                             # This is a boolean          bool()
variable5 = 3.14                              # This is a float or double float()
variable3 = [1, 2, 3, 4, 5]                   # This is a list


def print_variable_types():
    print('Type of variable1:', type(variable1), variable1)  # Output: <class 'int'>
    print('Type of variable2:', type(variable2), variable2)  # Output: <class 'str'>
    print('Type of variable3:', type(variable3), variable3)  # Output: <class 'list'>


print_variable_types()