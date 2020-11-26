# How to Transfer Files in the Network using Sockets in Python
# https://www.thepythoncode.com/article/send-receive-files-using-sockets-python

# https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications
# https://medium.com/better-programming/how-to-create-a-websocket-in-python-b68d65dbd549

# In order to communicate using the WebSocket protocol, you need to create a WebSocket object;
# this will automatically attempt to open the connection to the server.


'''
pip install websocket-client
pip install websockets

https://realpython.com/python-sockets/
https://exchange.blockchain.com/api/#introduction
https://www.blockchain.com/api

'''

from websocket import create_connection


options = {}


options['origin'] = 'https://exchange.blockchain.com'
url = "wss://ws.prod.blockchain.info/mercury-gateway/v1/ws"
ws = create_connection(url, **options)
msg = '{"token": "{API_SECRET}", "action": "subscribe", "channel": "auth"}'
ws.send(msg)
result =  ws.recv()
print(result)
# { "seqnum":0,
#   "event":"subscribed",
#   "channel":"auth",
#   "readOnly":false }
ws.close()


