from aiohttp import web

async def handle(request):
    return web.Response(text="Привет мир! Это асинхронный сервер на aiohttp.")

app = web.Application()
app.router.add_get("/", handle)

web.run_app(app, port=8080)

