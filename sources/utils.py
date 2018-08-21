from lxml import html
import requests
import os


def get_links():
    """
    Get all link from a website

    :return:
    """
    page = requests.get('https://www.wallpaper.com/latest')
    tree = html.fromstring(page.content)
    links = tree.xpath('//img/@src')
    return links


def download_link(link):
    download_path = "{}/images/{}".format(os.path.dirname(os.path.realpath(__file__)), os.path.basename(link))
    print("Downloading: {}".format(link))
    res = requests.get(link)
    with open(download_path, 'wb') as f:
        for chunk in res.iter_content(chunk_size=512 * 1024):
            if chunk:
                f.write(chunk)