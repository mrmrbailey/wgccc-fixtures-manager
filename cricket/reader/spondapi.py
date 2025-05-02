import asyncio
from config import username, password

from spond import spond

async def main():
    s = spond.Spond(username=username, password=password)
    groups = await s.get_groups()
    for group in groups:
         print(group)
    await s.clientsession.close()

asyncio.run(main())
