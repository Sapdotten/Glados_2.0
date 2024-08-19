from config.settings import engine, Base

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
async def create_table(table):
    async with engine.begin() as conn:
        await conn.run_sync(table.metadata.create_all)

async def drop_table(table):
    async with engine.begin() as conn:
        await conn.run_sync(table.drop(engine))

async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)