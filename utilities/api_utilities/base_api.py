import requests


class BaseAPI:
    def __init__(self, environment):
        self.__token = None
        self.__base_url = environment.base_api
        self.__headers = {'Accept': '*/*', 'Content-Type': 'application/json'}
        self.__request = requests

    @property
    def token(self):
        """Token Value"""
        return self.__token

    @token.setter
    def token(self, new_token):
        self.__token = new_token
        self.__headers['Cookie'] = f'token={self.__token}'

    def __headers_setup(self, headers=None):
        if headers is None:
            headers = self.__headers
        return headers

    def __url_setup(self, url):
        return f'{self.__base_url}{url}'

    def get(self, url, headers=None):
        return self.__request.get(self.__url_setup(url), headers=self.__headers_setup(headers))

    def post(self, url, body, headers=None):
        return self.__request.post(self.__url_setup(url), json=body, headers=self.__headers_setup(headers))

    def put(self, url, body, headers=None):
        return self.__request.put(self.__url_setup(url), json=body, headers=self.__headers_setup(headers))

    def patch(self, url, body, headers=None):
        return self.__request.patch(self.__url_setup(url), json=body, headers=self.__headers_setup(headers))

    def delete(self, url, headers=None):
        return self.__request.delete(self.__url_setup(url), headers=self.__headers_setup(headers))
