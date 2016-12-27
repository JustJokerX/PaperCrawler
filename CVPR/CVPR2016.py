#coding=utf-8
"""
This file is used to make a crawl
"""
import re
import urllib
import os

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
    dir_name = 'CVPR2016'
    if os.path.exists(dir_name) is False:
        os.mkdir(dir_name)
    for pdfurl in pdflist:
        reg2 = r'papers/(.+?\.pdf)'
        pdfre2 = re.compile(reg2)
        filename = dir_name + '/'+ re.findall(pdfre2, pdfurl)[0]
        print 'http://www.cv-foundation.org/openaccess/'+pdfurl
        if os.path.exists(filename) is True:
            print 'Exist'
        else:
            urllib.urlretrieve('http://www.cv-foundation.org/openaccess/'+pdfurl, filename)


HTML = get_html("http://www.cv-foundation.org/openaccess/CVPR2016.py")
print get_pdf(HTML)
