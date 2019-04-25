import contextvars

name = contextvars.ContextVar("name")
contexts = list()


def greet():
    print(f"Hello {name.get()}")


# Construct contexts and set the context variable name
for first_name in ["Steve", "Dina", "Harry"]:
    ctx = contextvars.copy_context()
    ctx.run(name.set, first_name)
    contexts.append(ctx)

# Run greet function inside each context
for ctx in reversed(contexts):
    ctx.run(greet)
