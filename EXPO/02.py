"""
Why do the following 3 code snippets behave differently
"""

# 1
items = [1, 2, 3, 4, 5, 6]
idx, item = None, None

for idx, item in enumerate(items):
    del item
print(items)


# 2
items = [1, 2, 3, 4, 5, 6]
idx, item = None, None

for idx, item in enumerate(items):
    items.remove(item)
print(items)

# 3
items = [1, 2, 3, 4, 5, 6]
idx, item = None, None

for idx, item in enumerate(items[:]):
    items.remove(item)
print(items)

