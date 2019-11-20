from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse
from starlette.responses import JSONResponse
import uvicorn

import asyncio


async def index(request):
    return PlainTextResponse("Index Page")


async def example_stats(request):
    return JSONResponse({'stats': [1, 0, 2, 3]})


async def health(request):
    return JSONResponse({'Application status': 200})


routes = [
    Route('/', index),
    Route('/stats', example_stats),
    Route('/health', health)
]

app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)