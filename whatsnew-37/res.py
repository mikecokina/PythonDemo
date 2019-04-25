from importlib import resources

with resources.open_text("data", "file.txt") as fid:
    c = fid.readlines()
    print(", ".join(c))
