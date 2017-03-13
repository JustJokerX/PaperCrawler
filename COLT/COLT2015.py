# coding=utf-8
"""
This file is used to make a crawl
"""
import __init__
import os
import re
import urllib

from utility import prgbar


def get_html(url):
    """Get the html """
    page = urllib.urlopen(url)
    html = page.read()
    return html


def get_pdf(html):
    """ xxx"""
    reg = r'href="(.+?\.pdf)">pdf'
    pdfre = re.compile(reg)
    pdflist = re.findall(pdfre, html)
    dir_name = 'COLT2015'
    maxrows = len(pdflist)
    pbar = prgbar.ProgressBar(total=maxrows)

    if os.path.exists(dir_name) is False:
        os.mkdir(dir_name)

    for idx, pdfurl in enumerate(pdflist):
        filename = dir_name + '/' + pdfurl
        pbar.log('http://jmlr.org/proceedings/papers/v40/' + pdfurl)
        if os.path.exists(filename) is True:
            pbar.log('Exist')
        else:
            urllib.urlretrieve(
                'http://jmlr.org/proceedings/papers/v40/' + pdfurl, filename)
        pbar.update(index=(idx + 1))

    pbar.finish()


if __name__ == '__main__':
    HTML = get_html("http://jmlr.org/proceedings/papers/v40/")
    print(get_pdf(HTML))
