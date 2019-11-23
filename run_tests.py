import time

from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession


def test_routes(routes):

    with FuturesSession() as session:

        futures = [session.get(route) for route in routes]

        start = time.time()
        for future in as_completed(futures):
            response = future.result()
            print(response.text)
            print(f'Response time elapsed: {response.elapsed.total_seconds()} seconds')
        end = time.time()

    return end - start


def async_test():

    async_routes = [
        'http://0.0.0.0:8000/example_async_blocker_one',
        'http://0.0.0.0:8000/example_async_blocker_two'
    ]

    return test_routes(async_routes)


def sync_test():

    sync_routes = [
        'http://0.0.0.0:8000/example_sync_blocker_one',
        'http://0.0.0.0:8000/example_sync_blocker_two'
    ]

    return test_routes(sync_routes)


print(f'Async routes took: {async_test()}')
print(f'Sync routes took: {sync_test()}')
