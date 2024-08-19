from config.settings import async_session

from .models import Gulfiks

async def add_gulfik():
    async with async_session() as session:
        async with session.begin():
            new_gulfik = Gulfiks(gulfik_model_name="ed", gulfik_model_descriptions="Ed Jones", gulfik_model_size=10)
            session.add(new_gulfik)
            await session.commit()
