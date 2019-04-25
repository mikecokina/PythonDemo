"""
Why do the following two code snippets behave differently
"""

# 1
x = [1, 2, 3]
y = x
x = x + [4, 5, 6]
print(x, y)


# 2
x = [1, 2, 3]
y = x
x += [4, 5, 6]
print(x, y)
