import requests
import re
from ..config import Config
from messages import SuccessMessages, ErrorMessages
from ..handler.logger.log import log_data_to_file
from ..handler.errors import TimeoutRequest

WORDPRESS_DEFAULT_DIRS = [
    "/wp-includes/js/jquery/jquery.js",
    "/wp-content/",
    "/wp-includes/",
    "/wordpress/"
]
CONFIG = Config()

class Wordpress(SuccessMessages, Config):
    def __init__(self) -> None:
        print(self.START_WORDPRESS_MODULE) # starting wordpress module

    @staticmethod
    def detect_wordpress(url: str) -> bool:
        """
        detects if the server is running Wordpress

        Args:
            url: (str)

        Return:
            bool: True / False
        """
        try:
            request = requests.get(f"{url}/", timeout=CONFIG.timeouts(), headers={"User-Agent": CONFIG.useragent()}).text
            for dirs in WORDPRESS_DEFAULT_DIRS:
                if dirs in request:
                    return True
            return False
        except requests.exceptions.ConnectionError:
            return print(ErrorMessages.CONNECTION_ERROR)

    @staticmethod
    def detect_wordpress_user(url: str) -> str:
        try:
            getuser = requests.get(f"{url}/?author=1", timeout=CONFIG.timeouts(), headers={"User-Agent": CONFIG.useragent()})
            matches = re.search(re.compile(r'author/(\w+)?/'), getuser.text)
            matches_url = re.search(re.compile(r'/author/(\w+)?/'), getuser.url)
            if matches:
                log_data_to_file(matches.group(1), "detect", "users")
                return print(f"{SuccessMessages.FOUND_WORDPRESS_USER} {matches.group(1)}")
            elif matches_url:
                log_data_to_file(matches_url.group(1), "detect", "users")
                return print(f"{SuccessMessages.FOUND_WORDPRESS_USER} {matches_url.group(1)}")
            return print(ErrorMessages.NO_WORDPRESS_USER)
        except requests.exceptions.ConnectionError:
            return print(ErrorMessages.CONNECTION_ERROR)

    @staticmethod
    def detect_wordpress_version(url: str) -> str:
        try:
            get_version = requests.get(url, timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()}).text
            version_search = re.search(re.compile(r'content=\"WordPress (\d{0,9}.\d{0,9}.\d{0,9})?\"'), get_version)
            if version_search:
                log_data_to_file(version_search.group(1), "detect", "version")
                return print(f"{SuccessMessages.FOUND_WORDPRESS_VERSION} {version_search.group(1)}")
            return print(ErrorMessages.NO_WORDPRESS_VERSION)
        except requests.exceptions.ConnectionError:
            return print(ErrorMessages.CONNECTION_ERROR)

    @staticmethod
    def detect_wordpress_themes(url: str) -> str:
        try:
            themes_array = []
            get_themes = requests.get(url, timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()}).text
            theme_matches = re.findall(re.compile(r'themes/(\w+)?/'), get_themes)
            if len(theme_matches) > 0:
                themes = ', '.join(theme_matches)
                log_data_to_file(themes, "detect", "themes")
                return print(f"{SuccessMessages.FOUND_WORDPRESS_THEME}{themes}")
            return print(ErrorMessages.NO_WORDPRESS_THEMES)
        except requests.exceptions.ConnectionError:
            return print(ErrorMessages.CONNECTION_ERROR)

    @staticmethod
    def detect_wordpress_plugins(url: str) -> str:
        try:
            plugins_array = []
            get_plugins = requests.get(url, timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()}).text
            plugin_matches = re.findall(re.compile(r'wp-content/plugins/(\w+)?/'), get_plugins)
            if len(plugin_matches) > 0:
                plugins = ', '.join(plugin_matches)
                log_data_to_file(plugins, "detect", "plugin")
                return print(f"{SuccessMessages.FOUND_WORDPRESS_PLUGINS}{plugins}")
            return print(ErrorMessages.NO_WORDPRESS_PLUGINS)
        except requests.exceptions.ConnectionError:
            return print(ErrorMessages.CONNECTION_ERROR)

