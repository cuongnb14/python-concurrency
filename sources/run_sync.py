from utils import get_links, download_link
from time import time

if __name__ == '__main__':
    start_time = time()
    for link in get_links():
        download_link(link)
    print("Total time download: {}s".format(time() - start_time))