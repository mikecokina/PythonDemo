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

# #####################################
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")