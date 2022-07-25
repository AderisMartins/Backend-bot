from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy import delete, select, update

from database.models import Social
from database.connection import async_session


async def list_social():
    async with async_session() as session:
        q = select(Social)
        result = await session.execute(q)
        curr = result.scalars().all()
        return curr

async def show_social(id):
    async with async_session() as session:
        q = select(Social).where(Social.id == id)
        result = await session.execute(q)
        curr = result.scalar()
        return curr


async def create_social(social_media):
    async with async_session() as session:
        session.add(Social(social_media=social_media))
        await session.commit()


async def delete_social(id):
    async with async_session() as session:
        await session.execute(delete(Social).where(Social.id == id))
        await session.commit()


async def update_social(id, social):
    async with async_session() as session:
        q = update(Social).where(Social.id == id).values(social_media = social.social_media)
        await session.execute(q)
        await session.commit()


