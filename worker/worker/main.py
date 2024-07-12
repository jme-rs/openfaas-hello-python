import pymec
from pymec import api
import asyncio
from httpx import AsyncClient


async def main():
    client = (
        pymec.Client()
        .client(AsyncClient(timeout=20))
        .host("http://192.168.1.22/api/v0.5/")
    )

    
    


if __name__ == "__main__":
    asyncio.run(main())
