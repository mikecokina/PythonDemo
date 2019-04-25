# python.exe "PythonDemo\PEP-537\PEP 565\warning.py"

from warnings import warn


def dep():
    warn("dep warn", DeprecationWarning)


if __name__ == "__main__":
    dep()
