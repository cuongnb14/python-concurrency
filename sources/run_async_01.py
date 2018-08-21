"""
Download images asynchronous use multi threading

"""
from queue import Queue
from threading import Thread
from time import time

from utils import get_links, download_link


class DownloadWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            link = self.queue.get()
            try:
                download_link(link)
            finally:
                self.queue.task_done()


if __name__ == '__main__':
    ts = time()
    links = get_links()
    queue = Queue()
    # Create 8 worker threads
    for x in range(8):
        worker = DownloadWorker(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()

    for link in links:
        queue.put(link)
    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()

    print("Total time download: {}s".format(time() - ts))
