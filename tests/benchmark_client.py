import trio
from trio_websocket import open_websocket_url

async def main():
    async with open_websocket_url('ws://localhost:8000/foo') as ws:
        for i in range(100_000):
            await ws.get_message()

trio.run(main)