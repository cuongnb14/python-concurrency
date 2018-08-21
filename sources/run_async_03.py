"""
Download images asynchronous use concurrent.futures

"""
from concurrent.futures import ThreadPoolExecutor
from time import time

from utils import get_links, download_link

if __name__ == '__main__':
    ts = time()
    links = get_links()

    # By placing the executor inside a with block, the executors shutdown method
    # will be called cleaning up threads.
    #
    # By default, the executor sets number of workers to 5 times the number of
    # CPUs.
    with ThreadPoolExecutor(4) as executor:
        executor.map(download_link, links, timeout=30)

    print("Total time download: {}s".format(time() - ts))
