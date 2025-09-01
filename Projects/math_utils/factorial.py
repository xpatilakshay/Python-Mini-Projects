'''

📍 Concepts: Default args, Keyword args, *args, **kwargs, Recursion, Anonymous Functions (lambda), Modules, Packages.
📝 Task: Math Utilities Package

Create a math_utils package with:

factorial (recursion)

fibonacci (recursion)

power function (with default arg exponent=2)

sum_all(*args)

key_value_demo(**kwargs)

Import and test them in a main script.

'''

def factorial(num):
    if num<=1:
        return 1
    else:
        return factorial(num-1)*num
    