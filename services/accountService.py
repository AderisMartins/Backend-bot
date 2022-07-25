from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy import delete, select, update

from database.models import Account
from database.connection import async_session


async def list_account():
    async with async_session() as session:
        q = select(Account)
        result = await session.execute(q)
        curr = result.scalars().all()
        return curr

async def show_account(id):
    async with async_session() as session:
        q = select(Account).where(Account.id == id)
        result = await session.execute(q)
        curr = result.scalar()
        return curr

async def create_account(email, password, social_id):
    async with async_session() as session:
        session.add(Account(email=email, password=password, social_id=social_id))
        await session.commit()


async def delete_account(id):
    async with async_session() as session:
        await session.execute(delete(Account).where(Account.id == id))
        await session.commit()


async def update_account(id, account):
    async with async_session() as session:
        q = update(Account).where(Account.id == id).values(email = account.email, password = account.password, social_id = account.social_id)
        await session.execute(q)
        await session.commit()

