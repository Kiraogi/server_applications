from aiohttp import web

async def handle(request): # Асинхронный обработчик запросов
    return web.Response(text="Привет мир! Это асинхронный сервер на aiohttp.")

app = web.Application()
app.router.add_get("/", handle) # Регистрация запроса GET

web.run_app(app, port=8080) # Запуск сервера по порту 8080


