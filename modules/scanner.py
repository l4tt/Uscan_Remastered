from .recon.wordpress import Wordpress
from messages import ErrorMessages, SuccessMessages, DetectionMessages
from .config import Config
from .recon.host.host_info import HostInfo
from .recon.host.dns_records import DnsRecords

class Scanner(ErrorMessages, SuccessMessages, DetectionMessages):
    def __init__(self) -> None:
        self.CMS = False
        self.CONFIG = Config()

    def runner(self, url: str) -> None:
        """
            starts all uscan scanning modules

            Args:
                self: (Scanner) class
                url: (str)

            Return:
                None: (pass)
        """
        print(self.MAY_TAKE_A_SEC)
        self.load_modules()
        if self.CONFIG.enable_recon():
            print(self.START_HOST_RECON)
            self.cms_detect(self.detect_cms(url), url)
            self.host_headers(url)
            DnsRecords(url).dns_reslover()

    def detect_cms(self, url: str) -> str:
        if Wordpress.detect_wordpress(url): # static class method - returns bool, detects if (server) is running a content management system
            self.CMS = "Wordpress"
        return self.CMS


    def load_modules(self) -> None:
        Wordpress() # prints __init__ of wordpress module

    def cms_detect(self, cms_detection: bool, url: str) -> str:
        if not cms_detection:
            return print(self.NO_CMS)
        if cms_detection:
            return print(f"{self.SUCCESS_CMS}{self.CMS}")
        if self.CMS == "Wordpress":
            print(self.wordpress_modules(url))

    def host_headers(self, url: str) -> str:
        """
            detects host headers, MESSY CODE
            Args:
                self (object)
                url: str
            Returns:
                str
        """
        host_info = HostInfo(url)
        host_headers = [host for host in [host_info.content_type(), host_info.x_pingback(), host_info.get_server(), host_info.xss_protection(), 
                                          host_info.cross_origin(), host_info.strict_transport(), host_info.x_content_type(), host_info.content_security()] 
                        if host and print(f"{self.FOUND_HEADERS}{host}")]

        if host_info.detect_cloudflare():
            print(self.FOUND_CLOUDFLARE)


    def wordpress_modules(self, url: str) -> None:
        Wordpress.detect_wordpress_user(url)
        Wordpress.detect_wordpress_version(url)
        Wordpress.detect_wordpress_themes(url)
        Wordpress.detect_wordpress_plugins(url)