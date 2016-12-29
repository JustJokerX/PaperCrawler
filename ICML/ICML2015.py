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
    dir_name = 'ICML2015'
    if os.path.exists(dir_name) is False:
        os.mkdir(dir_name)
    for pdfurl in pdflist:
        filename = dir_name + '/' + pdfurl
        print 'http://jmlr.org/proceedings/papers/v37/' + pdfurl
        if os.path.exists(filename) is True:
            print 'Exist'
        else:
            urllib.urlretrieve('http://jmlr.org/proceedings/papers/v37/'+pdfurl, filename)


HTML = get_html("http://jmlr.org/proceedings/papers/v37/")
print get_pdf(HTML)
