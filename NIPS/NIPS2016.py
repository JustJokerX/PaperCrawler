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
    reg = r'href="/paper/(.+?)"'
    pdfre = re.compile(reg)
    pdflist = re.findall(pdfre, html)
    dir_name = 'NIPS2016'
    maxrows = len(pdflist)
    pbar = prgbar.ProgressBar(total=maxrows)

    if os.path.exists(dir_name) is False:
        os.mkdir(dir_name)

    for idx, pdfurl in enumerate(pdflist):
        filename = dir_name + '/' + pdfurl + '.pdf'
        pbar.log('http://papers.nips.cc/paper/' + pdfurl + '.pdf')
        if os.path.exists(filename) is True:
            pbar.log('Exist')
        else:
            urllib.urlretrieve(
                'http://papers.nips.cc/paper/' + pdfurl + '.pdf', filename)
        pbar.update(index=(idx + 1))

    pbar.finish()


if __name__ == '__main__':
    HTML = get_html(
        'http://papers.nips.cc/book/'
        'advances-in-neural-information-processing-systems-29-2016')
    print(get_pdf(HTML))
