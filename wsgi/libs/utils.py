__author__ = 'lorenzo@pramantha.net'

from base64 import b64encode, b64decode
from urllib.parse import urlparse


def encode_url(url):
    """
    Encodes an url in base64
    :param url: a string
    :return: a base64 string
    """
    return b64encode(str(url).encode(encoding='UTF-8')).decode(encoding='UTF-8')


def decode_url(enc):
    """
    Reverse of encode_url()
    :param enc: a base64 string
    :return: a string that is an url
    """
    return b64decode(str(enc)).decode(encoding='UTF-8')


def check_if_url(url):
    """
    Find out if a string is an url or not
    :param url: a string
    :return: boolean
    """
    check = urlparse(url)
    print(check)
    #print(url)
    if not all([check.scheme, check.netloc]) or check.scheme not in ['http', 'https', 'ftp']:
        #print(Exception('wrong url'))
        return False
    return True


