import asyncio

async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print("done fetching")
    return {'data': 1}

async def run_algorithm():
    for i in range(10):
        print("running algorithm")
        await asyncio.sleep(1)

async def main():
    data = asyncio.create_task(fetch_data())
    await run_algorithm()
    print(await data)

asyncio.run(main())




"""
    async def print_something():
    await asyncio.sleep(1)
    print("something")
    return "finished"

async def main():
    print("main")

    task = asyncio.create_task(print_something())

    print("main again")
    result = await task
    print(result)

asyncio.run(main())
 """
