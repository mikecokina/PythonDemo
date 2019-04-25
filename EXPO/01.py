"""
Why does the following code behave so strangely

py35:

    {0, 1, 2, 3, 4, 5, 6, 7}

py36, py37:

    {0, 1, 2, 3, 4}

"""

a = {0: 0}
b = list()

for i in a:
    del a[i]
    a[i+1] = 0
    b.append(i)

print(b)

