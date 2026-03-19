import asyncpg
import asyncio

async def fetch_users():
    conn = await asyncpg.connect("postgresql://user:password@localhost/dbname")
    rows = await conn.fetch("SELECT * FROM users")
    await conn.close()
    return rows

async def main():
    users = await fetch_users()
    for user in users:
        print(user)

asyncio.run(main())
