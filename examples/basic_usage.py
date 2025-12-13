import asyncio
from pyderiv import DerivClient

TOKEN = "PUT_YOUR_DERIV_TOKEN_HERE"


async def main():
    client = DerivClient(TOKEN)

    await client.connect()

    balance = await client.get_balance()
    print("Balance:", balance)

    await client.close()


asyncio.run(main())


