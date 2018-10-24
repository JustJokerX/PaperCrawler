# coding=utf-8
"""
This file is used to make a crawl
"""

import __init__
import os
import re
# import urllib
from six.moves import urllib
from utility import prgbar


def get_html(url):
    """Get the html """
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    return html


def get_pdf(html, reg, dir_name, prefix):
    """ xxx"""
    # reg = r'href="/paper/(.+?)"'
    pdfre = re.compile(reg)
    pdflist = re.findall(pdfre, html)
    # dir_name = 'NIPS2012'
    maxrows = len(pdflist)
    pbar = prgbar.ProgressBar(total=maxrows)

    if os.path.exists(dir_name) is False:
        os.mkdir(dir_name)

    for idx, pdfurl in enumerate(pdflist):
        filename = dir_name + '/' + pdfurl + '.pdf'
        pbar.log(prefix + pdfurl + '.pdf')
        if os.path.exists(filename) is True:
            pbar.log('Exist')
        else:
            urllib.request.urlretrieve(
                prefix + pdfurl + '.pdf', filename)
        pbar.update(index=(idx + 1))

    pbar.finish()


if __name__ == '__main__':
    HTML = get_html(
        'http://papers.nips.cc/book/'
        'advances-in-neural-information-processing-systems-25-2012')
    print(get_pdf(HTML, r'href="/paper/(.+?)"', 'NIPS2012', 'http://papers.nips.cc/paper/'))
