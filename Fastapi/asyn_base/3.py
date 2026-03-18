import asyncio

async def task_1():
    print("Задача 1 началась")
    await asyncio.sleep(2)
    print("Задача 1 завершена")

async def task_2():
    print("Задача 2 началась")
    await asyncio.sleep(1)
    print("Задача 2 завершена")

async def main():
    task1 = asyncio.create_task(task_1())
    task2 = asyncio.create_task(task_2())

    await task1
    await task2

asyncio.run(main())
