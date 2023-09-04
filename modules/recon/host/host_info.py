import requests

from ...config import Config
from ...handler.logger.log import log_data_to_file
from messages import SuccessMessages
from socket import gethostbyname


class HostInfo(SuccessMessages):

    def __init__(self, url: str) -> None:
        """
        walking down the street, distant memory's gone forever,
        take me to the magic of the moment where the children of tomarrow with you me,
        the wind of change blows straight
        """
        self.url = url
        self.CONFIG = Config()
        self.request = requests.get(f"{url}/", timeout=self.CONFIG.timeouts(), headers={"User-Agent": self.CONFIG.useragent()}).headers
        self.CLOUDFLARE = ['172', '104', '103', '173', '8']


    def content_type(self):
        try:
            log_data_to_file(self.request['Content-Type'], "info", "contentType")
            return self.request['Content-Type']
        except KeyError:
            return None

    def x_pingback(self):
        try:
            log_data_to_file(self.request['X-Pingback'], "info", "X_pingback")
            return self.request['X-Pingback']
        except KeyError:
            return None

    def get_server(self):
        try:
            log_data_to_file(self.request['Server'], "info", "Server")
            return self.request['Server']
        except KeyError:
            return None

    def strict_transport(self):
        try:
            log_data_to_file(self.request['Strict-Transport-Security'], "info", "Strict-Transport-Security")
            return self.request['Strict-Transport-Security']
        except KeyError:
            return None

    def content_security(self):
        try:
            log_data_to_file(self.request['Content-Security-Policy'], "info", "Content-Security-Policy")
            return self.request['Content-Security-Policy']
        except KeyError:
            return None

    def xss_protection(self):
        try:
            log_data_to_file(self.request['X-XSS-Protection'], "info", "X-XSS-Protection")
            return self.request['X-XSS-Protection']
        except KeyError:
            return None

    def x_content_type(self):
        try:
            log_data_to_file(self.request['X-Content-Type-Options'], "info", "X-Content-Type-Options")
            return self.request['X-Content-Type-Options']
        except KeyError:
            return None

    def cross_origin(self):
        try:
            log_data_to_file(self.request['Cross-Origin-Resource-Policy'], "info", "Cross-Origin-Resource-Policy")
            return self.request['Cross-Origin-Resource-Policy']
        except KeyError:
            return None

    def detect_cloudflare(self) -> bool:
        strip_url = self.url.replace("https://", "").replace("http://", "").replace("/", "")
        try:
            ip = gethostbyname(strip_url)
            if any(ip.startswith(cf) for cf in self.CLOUDFLARE):
                log_data_to_file(True, "info", "Cloudflare")
                return True
        except Exception:
            raise
        return False