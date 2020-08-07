from daniel_simplerequest import get_json, post_json
from error import RequestError
import pytest

def test_get_json():
    # no query string, no parent string
    r = get_json('https://httpbin.org/get')
    assert r['args'] == {}, 'response is not as expected'
    assert r['status'] // 100 == 2, 'status code should start with 2'

    # only query string
    r = get_json('https://httpbin.org/get?debug=true')
    assert r['args'] == {'debug': 'true'}, 'response is not as expected'
    assert r['status'] // 100 == 2, 'status code should start with 2'

    # only parameters
    r = get_json('https://httpbin.org/get', params={'name': '常⾒見見問題 Q&A'})
    assert r['args'] == {'name': '常⾒見見問題 Q&A'}, 'response is not as expected'
    assert r['status'] // 100 == 2, 'status code should start with 2'

    # both query string and parameters
    r = get_json('https://httpbin.org/get?debug=true', params={'name': '常⾒見見問題 Q&A'})
    assert r['args'] == {'debug': 'true', 'name': '常⾒見見問題 Q&A'}, 'response is not as expected'
    assert r['status'] // 100 == 2, 'status code should start with 2'

    # request fails
    with pytest.raises(RequestError) as e:
        assert get_json("https://httpbin.org/status/400"), 'should raise exception'
    assert e.value.status_code == 400, 'status code in request error should be 400'

    #invalid url
    with pytest.raises(ValueError) as e:
        assert get_json("google"), 'should raise exception'


def test_post_json():
    # both params and data
    data = {'isbn': '9789863479116', 'title': '流暢的 Python'}
    r = post_json('https://httpbin.org/post', params={'debug': 'true'}, data=data)
    assert r['args'] == {'debug': 'true'}, 'params should be passed successfully'
    assert r['json'] == data, 'data should be passed successfully'
    assert r['headers']['Content-Type'] == 'application/json', 'content type should be included in headers'

    # data is empty
    r = post_json('https://httpbin.org/post', params={'debug': 'true'})
    assert r['args'] == {'debug': 'true'}, 'params should be passed successfully'
    assert r['json'] == {}, 'data should be passed successfully'
    assert r['headers']['Content-Type'] == 'application/json', 'content type should be included in headers'


    # params is None
    data = {'isbn': '9789863479116', 'title': '流暢的 Python'}
    r = post_json('https://httpbin.org/post', data=data)
    assert r['args'] == {}, 'params should be passed successfully'
    assert r['json'] == data, 'data should be passed successfully' 
    assert r['headers']['Content-Type'] == 'application/json', 'content type should be included in headers'
   
