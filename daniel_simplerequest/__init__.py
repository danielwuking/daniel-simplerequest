import sys
import http.client
import json
from urllib.parse import urlparse
from error import RequestError
from request import get_target_path, parse_json_response, validate_url

def _make_request(method, type, url, params={}, data={}):
    parsed_url = urlparse(url)
    validate_url(parsed_url)

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
