import asyncio
import json
import websockets

from .exceptions import AuthorizationError, ConnectionError


DERIV_WS_URL = "wss://ws.derivws.com/websockets/v3?app_id=1089"


class DerivClient:
    def __init__(self, token: str):
        self.token = token
        self.ws = None

    async def connect(self):
        try:
            self.ws = await websockets.connect(DERIV_WS_URL)
            await self._authorize()
        except Exception as e:
            raise ConnectionError(str(e))

    async def _authorize(self):
        await self.send({
            "authorize": self.token
        })
        response = await self.receive()

        if "error" in response:
            raise AuthorizationError(response["error"]["message"])

    async def send(self, data: dict):
        if not self.ws:
            raise ConnectionError("Not connected to Deriv WebSocket")
        await self.ws.send(json.dumps(data))

    async def receive(self) -> dict:
        if not self.ws:
            raise ConnectionError("Not connected to Deriv WebSocket")
        return json.loads(await self.ws.recv())

    async def get_balance(self):
        await self.send({"balance": 1})
        return await self.receive()

    async def buy(self, proposal_id: str, price: float):
        await self.send({
            "buy": proposal_id,
            "price": price
        })
        return await self.receive()

    async def sell(self, contract_id: int, price: float = 0):
        await self.send({
            "sell": contract_id,
            "price": price
        })
        return await self.receive()

    async def close(self):
        if self.ws:
            await self.ws.close()
            self.ws = None
 