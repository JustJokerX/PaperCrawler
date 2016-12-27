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
    reg = r'href="/paper/(.+?)"'
    pdfre = re.compile(reg)
    pdflist = re.findall(pdfre, html)
    dir_name = 'NIPS2015'
    if os.path.exists(dir_name) is False:
        os.mkdir(dir_name)
    for pdfurl in pdflist:
        filename = dir_name+'/'+ pdfurl+'.pdf'
        print 'http://papers.nips.cc/paper/'+pdfurl+'.pdf'
        if os.path.exists(filename) is True:
            print 'Exist'
        else:
            urllib.urlretrieve('http://papers.nips.cc/paper/'+pdfurl+'.pdf', filename)


HTML = get_html('http://papers.nips.cc/book/'
                'advances-in-neural-information-processing-systems-28-2015')
print get_pdf(HTML)
