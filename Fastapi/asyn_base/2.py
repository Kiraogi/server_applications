import asyncio

async def fetch_data():
    print("Запрос данных...")
    await asyncio.sleep(3)  # Имитация долгого запроса
    print("Данные получены!")

async def main():
    print("Начало работы")
    await fetch_data()
    print("Программа завершена")

asyncio.run(main())
