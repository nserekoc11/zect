# pyderiv

A simple async Python wrapper for the Deriv WebSocket API.

## Installation

```bash
pip install pyderiv
```

## Local development

Install dependencies for local development:

```bash
pip install -r requirements.txt
pip install -e .
```

## Usage

Create a short script using your Deriv token:

```python
import os
import asyncio
from pyderiv import DerivClient

TOKEN = os.environ.get("DERIV_TOKEN")

async def main():
    client = DerivClient(TOKEN)
    await client.connect()
    balance = await client.get_balance()
    print("Balance:", balance)
    await client.close()

asyncio.run(main())
```

Set the token and run the example:

```bash
export DERIV_TOKEN="YOUR_TOKEN"
python -m examples.basic_usage
```