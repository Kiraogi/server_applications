from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/data")
async def get_data():
    await asyncio.sleep(2)  # Имитация долгой операции
    return {"message": "Данные загружены!"}

async def fetch_data():
    print("Запрос к базе данных...")
    await asyncio.sleep(2)
    print("Данные получены!")

async def fetch_api():
    print("Запрос к внешнему API...")
    await asyncio.sleep(3)
    print("Ответ API получен!")

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(fetch_api())

    await task1
    await task2

asyncio.run(main())
