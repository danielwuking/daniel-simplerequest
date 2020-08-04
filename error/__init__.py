class RequestError(Exception):
    def __init__(self, error_message, status_code):
        self.error_message = error_message
        self.status_code = status_code