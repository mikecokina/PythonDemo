import asyncio


async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)


async def run():
    async for p in ticker(.5, 10):
        print(p)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()
