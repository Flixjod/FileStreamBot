from aiohttp import web
from .stream_routes import routes

def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

@routes.get("/health", allow_head=True)
async def health_check_handler(_):
    return web.Response(status=200)

