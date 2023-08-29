import dns.resolver
from messages import SuccessMessages, ErrorMessages

class DnsRecords:
    def __init__(self, url: str) -> None:
        self.url = url
        self.striped_url = self.url.replace("https://", "").replace("http://", "").replace("/", "")

    def dns_reslover(self):
        try:
            AA = dns.resolver.resolve(self.striped_url, 'A')
            MX = dns.resolver.resolve(self.striped_url, 'MX')
            NS = dns.resolver.resolve(self.striped_url, 'NS')
            TXT = dns.resolver.resolve(self.striped_url, 'TXT')

            A_RECORD = [arecord for arecord in AA if arecord
                        and print(f"{SuccessMessages.FOUND_A_RECORD}{arecord}")]
            MX_RECORD = [mxrecord for mxrecord in MX if mxrecord
                        and print(f"{SuccessMessages.FOUND_MX_RECORD}{mxrecord}")]
            TXT_RECORD = [txtrecord for txtrecord in TXT if txtrecord
                        and print(f"{SuccessMessages.FOUND_TXT_RECORD}{txtrecord}")]
            NS_RECORD = [nsrecord for nsrecord in NS if nsrecord
                        and print(f"{SuccessMessages.FOUND_NS_RECORD}{nsrecord}")]
        except (dns.resolver.NoNameservers) as e:
            print(e)
            return print(ErrorMessages.NO_NAME_SERVER)