import asyncio

async def handle_client(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    print(f"Получено: {message}")

    writer.write(f"Эхо: {message}".encode())
    await writer.drain()

    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

asyncio.run(main())
