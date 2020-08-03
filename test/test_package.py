from error import error

def test_error_func():
    err = error()
    assert err.error_msg is "default_message"
