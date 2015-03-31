"""
JSON 2 HTML convertor
=====================

(c) Varun Malhotra 2013
http://softvar.github.io

Source Code: https://github.com/softvar/json2html-flask
------------

LICENSE: MIT
--------
"""

import json
from collections import OrderedDict
from html.parser import HTMLParser

from wsgi.libs.utils import encode_url, check_if_url

a = ''


def get_html_table(text):
    """
    receive submitted data and process
    """

    style = "<table class=\"table table-condensed table-bordered table-hover\">"

    try:
        ordered_json = json.loads(text, object_pairs_hook=OrderedDict)
        #print(ordered_json)
        processed_text = html_convertor(ordered_json, style)

        html_parser = HTMLParser()
        global a
        a = ''
        return html_parser.unescape(processed_text)
    except Exception as e:
        raise e


def iter_json(ordered_json, style):
    global a
    a = a + style
    for k, v in ordered_json.items():
        a += '<tr>'
        a = a + '<th>' + str(k) + '</th>'
        if v is None:
            v = ""
        if isinstance(v, list):
            a += '<td><ul>'
            for i in range(0, len(v)):
                if isinstance(v[i], str):
                    if check_if_url(v[i]):
                        hash = encode_url(v[i])
                        a = a + '<li><a href="/chronosapi/' + str(hash) + '">' + str(v[i]) + '</a></li>'
                    else:
                        a = a + '<li>' + v[i] + '</li>'
                elif isinstance(v[i], int) or isinstance(v, float):
                    a = a + '<li>' + str(v[i]) + '</li>'
                elif not isinstance(v[i], list):
                    iter_json(v[i], style)
                else:
                    a = a + '<li>' + ordered_json[i] + '</li>'
            a += '</ul></td>'
            a += '</tr>'
        elif isinstance(v, str):
            if k in ['dbpedia', 'wikiUrl']:
                a = a + '<td><a target="_blank" href="' + str(v) + '">' + str(v) + '</a></td>'
            elif check_if_url(v):
                hash = encode_url(v)
                a = a + '<td><a href="/chronosapi/' + str(hash) + '">' + str(v) + '</a></td>'
            else:
                a = a + '<td>' + str(v) + '</td>'
            a += '</tr>'
        elif isinstance(v, int) or isinstance(v, float):
            a = a + '<td>' + str(v) + '</td>'
            a += '</tr>'
        else:
            a += '<td>'
            iter_json(v, style)
            a += '</td></tr>'
    a += '</table>'


def html_convertor(ordered_json, style):
    """
    converts JSON Object into human readable HTML representation
    generating HTML table code with raw/bootstrap styling.
    """

    global a
    try:
        for k, v in ordered_json.items():
            pass
        iter_json(ordered_json, style)
    except Exception as e:
        print(e)
        for i in range(0, len(ordered_json)):
            if isinstance(ordered_json[i], str):
                a = a + '<li>' + ordered_json[i] + '</li>'
            elif isinstance(ordered_json[i], int) or isinstance(ordered_json[i], float):
                a = a + '<li>'+ str(ordered_json[i]) + '</li>'
            elif not isinstance(ordered_json[i], list):
                html_convertor(ordered_json[i], style)


    return a

