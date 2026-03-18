import asyncio

async def handle_request():
    print("Обработка запроса...")
    await asyncio.sleep(2)  # Имитация задержки
    print("Запрос обработан!")

async def main():
    task1 = asyncio.create_task(handle_request())
    task2 = asyncio.create_task(handle_request())

    await task1
    await task2

asyncio.run(main())
