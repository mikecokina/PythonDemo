def do(e, f):
    # following possibilities (1) and (2) to debug program are eqiuvalent
    # (1)
    # import pdb; pdb.set_trace()
    # (2)
    # breakpoint()
    return f / e
    
a, b = 0, 1
print(do(a, b))
