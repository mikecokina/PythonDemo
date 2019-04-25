from warnings import warn

deprecated = ['old_function', 'old_other_function']


def old_fn(*args, **kwargs):
    warn('old_fn is deprecated function', DeprecationWarning)


def _deprecated_old_function(*args, **kwargs):
    print("invoked deprecated_old_function")


def _deprecated_old_other_function(*args, **kwargs):
    print("invoked deprecated_old_other_function")


def __getattr__(name):
    if name in deprecated:
        warn(f'{name} is deprecated', DeprecationWarning)
        return globals()[f'_deprecated_{name}']
    raise AttributeError(f'module {__name__} has no attribute {name}')
