"""
Download images asynchronous use native coroutine

"""
from time import time
import aiohttp
import os
import asyncio

from utils import get_links


async def async_download_link(session, link):
    """
    Async version of the download_link method we've been using in the other examples.
    :param session: aiohttp ClientSession
    :param link: the url of the link to download
    :return:
    """
    download_path = "{}/images/{}".format(os.path.dirname(os.path.realpath(__file__)), os.path.basename(link))
    print("Downloading: {}".format(link))
    async with session.get(link) as response:
        with open(download_path, 'wb') as f:
            while True:
                # await pauses execution until the 1024 (or less) bytes are read from the stream
                chunk = await response.content.read(1024)
                if not chunk:
                    # We are done reading the file, break out of the while loop
                    break
                f.write(chunk)


async def main():
    # We use a session to take advantage of tcp keep-alive
    # Set a 3 second read and connect timeout. Default is 5 minutes
    async with aiohttp.ClientSession(conn_timeout=3, read_timeout=3) as session:
        tasks = [(async_download_link(session, link)) for link in get_links()]
        # gather aggregates all the tasks and schedules them in the event loop
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    ts = time()
    # Create the asyncio event loop
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        # Shutdown the loop even if there is an exception
        loop.close()

    print("Total time download: {}s".format(time() - ts))
