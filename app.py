import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=r'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


# from aiohttp import web

# async def handle(request):
#     name = request.match_info.get('name', "Anonymous")
#     text = "Hello, " + name
#     return web.Response(text=text)

# async def wshandler(request):
#     ws = web.WebSocketResponse()
#     await ws.prepare(request)

#     async for msg in ws:
#         if msg.type == web.MsgType.text:
#             await ws.send_str("Hello, {}".format(msg.data))
#         elif msg.type == web.MsgType.binary:
#             await ws.send_bytes(msg.data)
#         elif msg.type == web.MsgType.close:
#             break

#     return ws


# app = web.Application()
# app.router.add_get('/echo', wshandler)
# app.router.add_get('/', handle)
# app.router.add_get('/{name}', handle)

# web.run_app(app)