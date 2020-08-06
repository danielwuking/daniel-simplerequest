import sys
import http.client
import json
from urllib.parse import urlparse
from error import RequestError
from request import get_target_path, parse_json_response

def _make_request(method, type, url, params={}, data={}):
    parsed_url = urlparse(url)
    path = get_target_path(parsed_url, params)

    conn = http.client.HTTPSConnection(parsed_url.hostname)
    if type == 'json':
        data = json.dumps(data)

    if method == 'GET':
        conn.request('GET', path)
    elif method == 'POST':
        headers = {'Content-Type': 'application/json'}
        conn.request('POST', path, body=data, headers=headers)

    response = conn.getresponse()
    if response.status // 100 != 2:
        exception = RequestError('HTTP Status Code: ' + str(response.status), response.status)
        sys.last_value = exception
        raise exception

    if type == 'json':
        return parse_json_response(response)

    return response


def get_json(url, params={}):
    return _make_request('GET', 'json', url, params)

def post_json(url, params={}, data={}):
    return _make_request('POST', 'json', url, params, data)


get_json('https://httpbin.org/get?debug=true', params={'name': '常⾒見見問題 Q&A'})
data = {'isbn': '9789863479116', 'title': '流暢的 Python'}
post_json('https://httpbin.org/post', params={'debug': 'true'}, data=data)

