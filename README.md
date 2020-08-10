# daniel-simplerequest

## Description

A simple Python request package based on standard libraries.

You can install the package via pip command below from Test PyPI.

```python
pip install -i https://test.pypi.org/simple/ daniel-simplerequest
```

## Instruction

Import the package to your python3 code and run the code below.

```python
daniel_simplerequest.get_json(url, params)
daniel_simplerequest.post_json(url, params, data)
```

url: url for the request object

params: parameters to send in the query string of the request(optional)

data: data to send in the request(optional)

## Example

```python
from daniel_simplerequest import get_json, post_json

#GET request
r = get_json('https://httpbin.org/get')
print(r['args'])
# {}

#GET request with query string and parameters
r = get_json('https://httpbin.org/get?debug=true', params={'name': '常⾒見見問題 Q&A'})
print(r['args'])
# {'debug': 'true', 'name': '常⾒見見問題 Q&A'}

#POST request with query string and parameters
data = {'isbn': '9789863479116', 'title': '流暢的 Python'}
r = post_json('https://httpbin.org/post', params={'debug': 'true'}, data=data)
print(r['args'])
print(r['json']) 
# {'debug': 'true'}
# {'isbn': '9789863479116', 'title': '流暢的 Python'}

```
