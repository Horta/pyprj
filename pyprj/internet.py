from __future__ import unicode_literals

import re
import requests


try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

def absolute_url(url):
    i = url.find('/../') + 1
    return urljoin(url[:i], url[i:])

def internet_content(url, type_='text'):
    resp = requests.get(url)
    if resp.ok:
        return getattr(resp, type_)
    msg = "Failure while requesting %s: " % url
    raise RuntimeError(msg + str(resp.status_code))

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext.replace("&nbsp;", "")