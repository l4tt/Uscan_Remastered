from .recon.wordpress import Wordpress
from .config import Config
from .recon.host.host_info import HostInfo
from .recon.host.dns_records import DnsRecords
from .handler.logger.log import log_data_to_file
from messages import SuccessMessages, ErrorMessages, DetectionMessages

class Scanner(SuccessMessages, ErrorMessages, DetectionMessages):
    def __init__(self) -> None:
        self.CMS = False
        self.CONFIG = Config()

    def runner(self, url: str) -> None:
        """
        Starts all uscan scanning modules

        Args:
            self: (Scanner) class
            url: (str)

        Return:
            None: (pass)
        """
        print(self.MAY_TAKE_A_SEC)
        print(self.LOAD_MODULES)
        self.load_modules()
        if self.CONFIG.enable_recon():
            print(self.START_HOST_RECON)
            self.cms_detect(self.detect_cms(url)[0], url)
            self.host_headers(url)
            print(self.START_DNS_SEARCH)
            DnsRecords(url).dns_resolver()
            log_data_to_file(url, None, True)

    def detect_cms(self, url: str) -> str:
        if Wordpress.detect_wordpress(url):
            self.CMS = "Wordpress"

        return (self.CMS, log_data_to_file(self.CMS, "detect", "cms"))

    def load_modules(self) -> None:
        return Wordpress()

    def cms_detect(self, cms_detection: bool, url: str) -> str:
        if not cms_detection:
            return print(self.NO_CMS)
        if cms_detection:
            print(f"{self.SUCCESS_CMS}{self.CMS}")
            if self.CMS == "Wordpress":
                self.wordpress_modules(url)
            elif self.CMS == "Joomla":
                ...
                #self.joomla_modules(url)
            # Add more conditions for other CMSs and their respective modules

    def host_headers(self, url: str) -> str:
        """
        Detects host headers

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
        modules_to_run = [Wordpress.detect_wordpress_user(url), Wordpress.detect_wordpress_version(url), Wordpress.detect_wordpress_themes(url), Wordpress.detect_wordpress_plugins(url)]
        for module in modules_to_run:
            if module:
                module()
