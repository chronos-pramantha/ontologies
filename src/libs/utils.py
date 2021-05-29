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
    http://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python
    :param url: a string
    :return: boolean
    """
    check = urlparse(url)
    #print(check)
    #print(url)
    if not all([check.scheme, check.netloc]) or check.scheme not in ['http', 'https', 'ftp']:
        #print(Exception('wrong url'))
        return False
    return True


# def rdf_translate(params):
#     """
#     Translate
#     :param params: parameters in the request
#     :return: body of the response
#     """
#     import pycurl
#     from urllib.parse import urlencode
#     c = pycurl.Curl()
#     url = 'http://rdf-translator.appspot.com/convert/json-ld/nt/content'
#     c.setopt(c.URL, url)
#     # if request is GET
#     #if params: c.setopt(c.URL, url + '?' + urlencode(params))

#     # if request is POST
#     post_data = {'content': params}
#     # Form data must be provided already urlencoded.
#     postfields = urlencode(post_data)
#     # Sets request method to POST,
#     # Content-Type header to application/x-www-form-urlencoded
#     # and data to send in request body.
#     c.setopt(c.POSTFIELDS, postfields)

#     from io import BytesIO
#     buffer = BytesIO()

#     c.setopt(c.WRITEDATA, buffer)
#     c.perform()
#     c.close()
#     return buffer.getvalue().decode('utf-8')



