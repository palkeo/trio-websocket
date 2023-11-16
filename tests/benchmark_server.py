import trio
import sys

from trio_websocket import serve_websocket, ConnectionClosed


async def spam_server(request):
    message_size = int(sys.argv[1])
    message = b"A" * message_size
    ws = await request.accept()
    while True:
        try:
            await ws.send_message(message)
        except ConnectionClosed:
            break

async def main():
    await serve_websocket(spam_server, '127.0.0.1', 8000, ssl_context=None)

trio.run(main)