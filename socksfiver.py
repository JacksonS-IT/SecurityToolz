import requests
import random

def generate_proxy():
    # Generate a random IP address
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    port = random.randint(1024, 65535)
    return f"{ip}:{port}"

def check_proxy(proxy):
    try:
        response = requests.get("http://httpbin.org/ip", proxies={"http": f"socks5://{proxy}", "https": f"socks5://{proxy}"}, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def create_clean_socks5_proxies(num_proxies):
    clean_proxies = []
    while len(clean_proxies) < num_proxies:
        proxy = generate_proxy()
        if check_proxy(proxy):
            clean_proxies.append(proxy)
    return clean_proxies

if __name__ == "__main__":
    num_proxies_to_generate = 10
    clean_proxies = create_clean_socks5_proxies(num_proxies_to_generate)
    print("Clean SOCKS5 Proxies:")
    for proxy in clean_proxies:
        print(proxy)
