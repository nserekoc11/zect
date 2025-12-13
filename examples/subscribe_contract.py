import asyncio
from pyderiv import DerivClient

TOKEN = "PUT_YOUR_DERIV_TOKEN_HERE"
CONTRACT_ID = 123456789  # use a real contract id


async def main():
    client = DerivClient(TOKEN)
    await client.connect()

    print("Subscribing to contract updates...\n")

    async for update in client.subscribe_contract(CONTRACT_ID):
        print(update)

    print("\nContract settled.")
    await client.close()


asyncio.run(main())
