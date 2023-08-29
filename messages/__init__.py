from colorama import Fore

class SuccessMessages:
    SUCCESS_MESSAGES = f"{Fore.RESET}[ {Fore.GREEN}Success{Fore.RESET} ] "
    SUCCESS_CMS = f"{SUCCESS_MESSAGES}CMS:{Fore.YELLOW} "
    START_HOST_RECON = f"{Fore.RESET}═══════{Fore.LIGHTBLACK_EX}HOST INFO{Fore.RESET}═══════"
    START_WORDPRESS_MODULE = f"{SUCCESS_MESSAGES}{Fore.YELLOW}Loaded Wordpress module"
    FOUND_WORDPRESS_USER = f"{SUCCESS_MESSAGES}Wordpress User:{Fore.YELLOW}"
    FOUND_CONTENT_TYPE = f"{SUCCESS_MESSAGES}Content-Type:{Fore.YELLOW}"
    FOUND_PINGBACK = f"{SUCCESS_MESSAGES}X-Pingback:{Fore.YELLOW}"
    FOUND_SERVER = f"{SUCCESS_MESSAGES}Server:{Fore.YELLOW}"
    FOUND_HEADERS = f"{SUCCESS_MESSAGES}Found server header: {Fore.YELLOW}"
    START_HEADER_SEARCH = f"{SUCCESS_MESSAGES}{Fore.YELLOW}Started hostinfo module"
    FOUND_WORDPRESS_VERSION = f"{SUCCESS_MESSAGES}Found Wordpress user: {Fore.YELLOW}"
    FOUND_WORDPRESS_THEME  = f"{SUCCESS_MESSAGES}Found Wordpress themes: {Fore.YELLOW}"
    FOUND_WORDPRESS_PLUGINS = f"{SUCCESS_MESSAGES}Found Wordpress plugins: {Fore.YELLOW}"
    FOUND_A_RECORD = f"{SUCCESS_MESSAGES}Found Dns-Record-A:{Fore.YELLOW} "
    FOUND_MX_RECORD = f"{SUCCESS_MESSAGES}Found Dns-Record-MX:{Fore.YELLOW} "
    FOUND_TXT_RECORD = f"{SUCCESS_MESSAGES}Found Dns-Record-TXT:{Fore.YELLOW} "
    FOUND_NS_RECORD = f"{SUCCESS_MESSAGES}Found Dns-Record-NS:{Fore.YELLOW} "

class ErrorMessages:
    # Error messages for uscan
    WARNING = f"{Fore.RESET}[ {Fore.RED}Warning{Fore.RESET} ] "
    MISSING_CONFIG = f"{WARNING}{Fore.YELLOW}Missing config.json [this can cause a lot of issues!]"
    MISSING_MODULE = f"{WARNING}{Fore.YELLOW}Missing pip module,"
    GOV_CPL = f"{WARNING}[ By law you agree that all purposes of (uscan), will not be used to conduct cyber-attacks and therefore the creator of (uscan . Nano) will not be responsable for any actions that you the (user) may do with this software \nYou the user also agree to not resell this software since it is open-source and free to the public use ]"
    STARTING_USCAN = f"{WARNING}{Fore.YELLOW}To continue please agree to the following terms above (y/n) "
    MAY_TAKE_A_SEC = f"\n{WARNING}{Fore.LIGHTYELLOW_EX}this may take take a little to gather results, adjust timeouts to be faster\n"
    CONNECTION_ERROR = f"{WARNING}{Fore.RED}Connection error"
    NO_WORDPRESS_USER = f"{WARNING}Couldn't detect a Wordpress user"
    NO_CONTENT_TYPE = f"{WARNING}Couldn't detect server content-type"
    NO_PINGBACK = f"{WARNING}Couldn't detect server pingback"
    NO_SERVER = f"{WARNING}Couldn't detect server header"
    NO_WORDPRESS_VERSION = f"{WARNING}Couldn't detect Wordpress version"
    NO_WORDPRESS_THEMES = f"{WARNING}Couldn't detect Wordpress themes"
    NO_WORDPRESS_PLUGINS = f"{WARNING}Couldn't detect Wordpress plugins"
    NO_NAME_SERVER = f"{WARNING}Couldn't Detect DNS nameservers"
    
class DetectionMessages:
    # Detected missing file paths for uscan to operate
    DETECTED = f"{Fore.RESET}[ {Fore.YELLOW}Detected{Fore.RESET} ]"
    RESULTS_FILES = f"{DETECTED}{Fore.LIGHTBLACK_EX} Path:"
    THREADS_WARN = f"{DETECTED} having more than 30 threads may increase CPU usage!"
    USERAGENT_WARN = f"{DETECTED} note: changing the useragent may break the bing dorker"
    NO_CMS = f"{DETECTED} No CMS found [{Fore.LIGHTBLACK_EX}this may be a false postive{Fore.RESET}]"
    FOUND_CLOUDFLARE = f"{DETECTED} Cloudflare [this could block requests]"

class HelpMenu:
    from modules.config import Config
    # loads config, trys to parse items
    config = Config()
    banner = f"""
                ╦ ╦┌─┐┌─┐┌─┐┌┐┌
                ║ ║└─┐│  ├─┤│││
                ╚═╝└─┘└─┘┴ ┴┘└┘
                        \033[1;91m スキャナー\033[00m\n
             [ Threads {config.threads()} - Exploits 0 ]
               type help to see options
            """
    HELP = """\n       ╔══════════════════════════════════════════════════════════════╗
        1. normal scan [type 1] - [PROVIDE A SINGLE TARGET]
        2. dork scan [type 2] - [COLLECTS TARGETS USING DORKS AND SCANS]
        3. proxy gen [type 3] - [COLLECTS A PROXY LIST]
        4. version [type ver] - [RETURNS USCAN CURRENT VERSION]
        5. credits [type creds] - [RETURN USCAN CREDITS]
       ╚══════════════════════════════════════════════════════════════╝
    """
    MENU_SELECT = f"[{Fore.LIGHTYELLOW_EX}Uscan{Fore.RESET}] >> "
    MENU_SELECT_URL = f"[{Fore.LIGHTYELLOW_EX}Url{Fore.RESET}] >> "
    MENU_VERSION  = f"[{Fore.LIGHTYELLOW_EX}Version{Fore.RESET}] "
    MENU_CREDITS = f"""
    [{Fore.LIGHTYELLOW_EX}Credits{Fore.RESET}] - Nano, Checksum
    [{Fore.RED}Legal warning] - Discrediting Authors is a bad thing to do ...
    """