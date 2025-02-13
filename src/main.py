from src.app.repository.models import init_db, create_and_commit

async def main():
    await init_db()
    await create_and_commit()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())