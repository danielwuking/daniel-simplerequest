from urllib.parse import urlencode

def get_target_path(parsed_url, params): 
    params_str = urlencode(params)
    url = parsed_url.path + '?' + parsed_url.query if parsed_url.query != '' else parsed_url.path
    if len(params_str) > 0:
        url = url + '&' + params_str if '?' in url else url + '?' + params_str
    return url