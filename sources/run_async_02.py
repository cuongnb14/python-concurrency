"""
Download images asynchronous use multi processes

"""
from multiprocessing.pool import Pool
from time import time

from utils import get_links, download_link

if __name__ == '__main__':
    ts = time()
    links = get_links()
    with Pool(4) as p:
        p.map(download_link, links)

    print("Total time download: {}s".format(time() - ts))
