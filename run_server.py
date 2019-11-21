from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse
from starlette.responses import JSONResponse
import uvicorn

import time
import asyncio


async def index(request):
    return PlainTextResponse("Index Page")


async def example_stats(request):
    return JSONResponse({'stats': [1, 0, 2, 3]})


async def health(request):
    return JSONResponse({'Application status': 200})


async def example_async_blocker_one(request):
    await asyncio.sleep(5)
    return PlainTextResponse("First async response sent")


async def example_async_blocker_two(request):
    await asyncio.sleep(5)
    return PlainTextResponse("Second async response sent")


async def example_sync_blocker_one(request):
    time.sleep(5)
    return PlainTextResponse("First sync response sent")


async def example_sync_blocker_two(request):
    time.sleep(5)
    return PlainTextResponse("Second sync response sent")


routes = [
    Route('/', index),
    Route('/stats', example_stats),
    Route('/health', health),
    Route('/example_async_blocker_one', example_async_blocker_one),
    Route('/example_async_blocker_two', example_async_blocker_two),
    Route('/example_sync_blocker_one', example_sync_blocker_one),
    Route('/example_sync_blocker_two', example_sync_blocker_two)
]

app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)