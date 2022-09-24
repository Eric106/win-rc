import netifaces as NETIF


def get_default_ip():
    default_if = NETIF.gateways()['default'][NETIF.AF_INET][1]
    default_ip = NETIF.ifaddresses(default_if)[NETIF.AF_INET][0]['addr']
    return default_ip
