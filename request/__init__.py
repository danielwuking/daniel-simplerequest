from urllib.parse import urlencode
import json

def get_target_path(parsed_url, params): 
    params_str = urlencode(params)
    url = parsed_url.path + '?' + parsed_url.query if parsed_url.query != '' else parsed_url.path
    if len(params_str) > 0:
        url = url + '&' + params_str if '?' in url else url + '?' + params_str
    return url

def parse_json_response(response):
    res = json.loads(response.read())
    res['status'] = response.status
    return res

def validate_url(parsed_url):
    if parsed_url.scheme == '' and parsed_url.netloc == '':
        raise ValueError('input should be a valid url')