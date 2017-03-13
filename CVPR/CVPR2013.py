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
    dir_name = 'CVPR2013'
    maxrows = len(pdflist)
    pbar = prgbar.ProgressBar(total=maxrows)

    if os.path.exists(dir_name) is False:
        os.mkdir(dir_name)

    for idx, pdfurl in enumerate(pdflist):
        reg2 = r'papers/(.+?\.pdf)'
        pdfre2 = re.compile(reg2)
        filename = dir_name + '/' + re.findall(pdfre2, pdfurl)[0]
        pbar.log('http://www.cv-foundation.org/openaccess/' + pdfurl)
        if os.path.exists(filename) is True:
            pbar.log('Exist')
        else:
            urllib.urlretrieve(
                'http://www.cv-foundation.org/openaccess/' + pdfurl, filename)
        pbar.update(index=(idx + 1))

    pbar.finish()


if __name__ == '__main__':
    HTML = get_html("http://www.cv-foundation.org/openaccess/CVPR2013.py")
    print(get_pdf(HTML))
