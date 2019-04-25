import asyncio


async def ping_server(*args):
    pass


async def ping_local():
    return await ping_server('192.168.1.1')


@asyncio.coroutine
def load_file():
    pass

# SyntaxError: invalid syntax
# async = 1


# not necessary to define loop
asyncio.run(ping_local())
