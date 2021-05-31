__author__ = 'lorenzo'

#
# This is the base test for checking if all the ontologies' endpoints are serving properly
#
#

import unittest
import http.client
from urllib.parse import urlparse


class TestOntologiesService(unittest.TestCase):
    def test_isonline(self):
        from src.contexts import ONTOLOGIES

        def test_reponse(conn, response):
            if int(response.status) == 200:
                print("TRUE")
                assert True
            elif int(response.status) == 301:
                u = response.getheader('Location')
                p = urlparse(u).path[1:urlparse(u).path[1].find('/')]
                print(p)
                check_url(p, u)
            else:
                assert False

            return conn.close()

        def check_url(name, uri=None):
            if uri:
                parsed = urlparse(uri)
                conn = http.client.HTTPConnection(parsed.netloc)
                conn.request("GET", parsed.path)
                response = conn.getresponse()
                return test_reponse(conn, response)

            url = "ontologies.pramantha.net"
            query = "/" + name
            print(url, query)
            conn = http.client.HTTPConnection(url)
            conn.request("GET", query)
            response = conn.getresponse()
            print(response.status, response.reason, response.headers)
            return test_reponse(conn, response)

        for n in ONTOLOGIES.keys():
            check_url(n)