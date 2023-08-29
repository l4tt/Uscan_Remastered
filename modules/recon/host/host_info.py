import requests

from ...config import Config
from messages import SuccessMessages
from socket import gethostbyname


class HostInfo(SuccessMessages):

    def __init__(self, url: str) -> None:
        self.url = url
        self.CONFIG = Config()
        self.request = requests.get(f"{url}/", timeout=self.CONFIG.timeouts(), headers={"User-Agent": self.CONFIG.useragent()}).headers
        self.CLOUDFLARE = ['172', '104', '103', '173', '8']
        print(SuccessMessages.START_HEADER_SEARCH)


    def content_type(self):
        try:
            return self.request['Content-Type']
        except KeyError:
            return None

    def x_pingback(self):
        try:
            return self.request['X-Pingback']
        except KeyError:
            return None

    def get_server(self):
        try:
            return self.request['Server']
        except KeyError:
            return None

    def strict_transport(self):
        try:
            return self.request['Strict-Transport-Security']
        except KeyError:
            return None

    def content_security(self):
        try:
            return self.request['Content-Security-Policy']
        except KeyError:
            return None

    def xss_protection(self):
        try:
            return self.request['X-XSS-Protection']
        except KeyError:
            return None

    def x_content_type(self):
        try:
            return self.request['X-Content-Type-Options']
        except KeyError:
            return None

    def cross_origin(self):
        try:
            return self.request['Cross-Origin-Resource-Policy']
        except KeyError:
            return None

    def detect_cloudflare(self) -> bool:
        strip_url = self.url.replace("https://", "").replace("http://", "").replace("/", "")
        try:
            ip = gethostbyname(strip_url)
            if [cf for cf in self.CLOUDFLARE if ip.startswith(cf)]:
                return True
        except Exception as e:
            raise e
        return False