"""
Why does the first expression evaluate to True when the second and third evaluate to False
"""

print(0 == 0 in [0])
print((0 == 0) in [0])
print(0 == (0 in [0]))
