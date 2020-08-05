import sys
import http.client
import json
from urllib.parse import urlparse
from error import RequestError
from request import get_target_path

def _make_request(method, url, params={}, data={}):
    parsed_url = urlparse(url)
    path = get_target_path(parsed_url, params)

    conn = http.client.HTTPSConnection(parsed_url.hostname)

    if method == 'GET':
        conn.request('GET', path)
    elif method == 'POST':
        headers = {'Content-Type': 'application/json'}
        conn.request('POST', path, body=json.dumps(data), headers=headers)

    response = conn.getresponse()
    if response.status // 100 != 2:
        exception = RequestError('HTTP Status Code: ' + str(response.status), response.status)
        sys.last_value = exception
        raise exception

    res = json.loads(response.read())
    res['status'] = response.status
    return res


def get_json(url, params={}):
    return _make_request('GET', url, params)

def post_json(url, params={}, data={}):
    return _make_request('POST', url, params, data)
    
