from daniel_simplerequest import get_json, post_json
from error import RequestError

def test_get_json():
    # no query string, no parent string
    r = get_json('https://httpbin.org/get')
    assert r['args'] == {}, 'response is not as expected'
    assert r['status_code'] // 100 == 2, 'status code should start with 2'

    # only query string
    r = get_json('https://httpbin.org/get?debug=true')
    assert r['args'] == {'debug': 'true'}, 'response is not as expected'
    assert r['status_code'] // 100 == 2, 'status code should start with 2'

    # only parameters
    r = get_json('https://httpbin.org/get', params={'name': '常⾒見見問題 Q&A'})
    assert r['args'] == {'name': '常⾒見見問題 Q&A'}, 'response is not as expected'
    assert r['status_code'] // 100 == 2, 'status code should start with 2'

    # both query string and parameters
    r = get_json('https://httpbin.org/get?debug=true', params={'name': '常⾒見見問題 Q&A'})
    assert r['args'] == {'debug': 'true', 'name': '常⾒見見問題 Q&A'}, 'response is not as expected'
    assert r['status_code'] // 100 == 2, 'status code should start with 2'

    # request fails
    with pytest.raises(RequestError) as e:
        assert get_json("https://httpbin.org/status/400"), 'should raise exception'
    assert e.status_code == 400, 'status code in request error should be 400'


def test_post_json():
    # both params and data
    data = {'isbn': '9789863479116', 'title': '流暢的 Python'}
    r = post_json('https://httpbin.org/post', params={'debug': 'true'}, data=data)
    assert r['args'] == {'debug': 'true'}, 'params should be passed successfully'
    assert json.loads(r['json']) == data, 'data should be passed successfully'

    # data is empty
    data = {'isbn': '9789863479116', 'title': '流暢的 Python'}
    r = post_json('https://httpbin.org/post', params={'debug': 'true'})
    assert r['args'] == {'debug': 'true'}, 'params should be passed successfully'
    assert json.loads(r['json']) == data, 'data should be passed successfully'

    # params is None
    data = {'isbn': '9789863479116', 'title': '流暢的 Python'}
    r = post_json('https://httpbin.org/post', params={'debug': 'true'}, data=data)
    assert r['args'] == {'debug': 'true'}, 'params should be passed successfully'
    assert json.loads(r['json']) == data, 'data should be passed successfully'    
