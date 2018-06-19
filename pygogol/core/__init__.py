from collections import namedtuple
from google.auth.transport.requests import AuthorizedSession

Request = namedtuple("Request", ["method", "url", "headers", "body"])

class GoogleAPI:
    def __init__(self, creds):
        self.credentials = creds
        self.session = AuthorizedSession(creds)
    def send(self, req):
        return self.session.request(req.method, req.url, headers=req.headers, data=req.data)