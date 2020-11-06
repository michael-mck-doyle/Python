# How to Transfer Files in the Network using Sockets in Python
# https://www.thepythoncode.com/article/send-receive-files-using-sockets-python

# https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications
# https://medium.com/better-programming/how-to-create-a-websocket-in-python-b68d65dbd549

# In order to communicate using the WebSocket protocol, you need to create a WebSocket object;
# this will automatically attempt to open the connection to the server.

import asyncio
import logging
import websockets

logging.basicConfig(level=logging.INFO)


async def consumer_handler(websocket: WebSocketClientProtocol) ->None:
    async for message in websocket:
        log_message(message)


async def consume(hostname: str, port: int) -> None:
    websocket_resource_url = f"ws://{hostname}:{port}"
    async with websockets.connect(websocket_resource_url) as websocket:
        await consumer_handler(websocket)


def log_message(message: str) -> None:
    logging.info(f"Message: {message}")


