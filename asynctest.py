import asyncio

async def count():
    for i in [1,2,3,4,5]:
        print(i)
        await asyncio.sleep(1)
async def count2():
    for letter in "Andrew":
        print(letter)
        await asyncio.sleep(2)
async def main():
    await asyncio.gather(count(),count2()) # What does gather mean?


asyncio.run(main())
print("Done")
