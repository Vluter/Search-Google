import requests
import time

def get_ip_address():
    response = requests.get("https://api.ipify.org")
    return response.text

def get_user_agent():
    response = requests.get("https://randomuser.me/api/1.2/?nat=US")
    data = response.json()
    return data["results"][0]["useragent"]

def get_geo_location():
    response = requests.get("https://ipinfo.io/")
    data = response.json()
    return data["loc"]

def open_browser(keyword, domain):
    for i in range(10):
        ip_address = get_ip_address()
        user_agent = get_user_agent()
        geo_location = get_geo_location()

        command = f"termux-open-url https://www.young.my.id/?q={keyword}&ip={ip_address}&ua={user_agent}&loc={geo_location}"
        print(command)
        system(command)

def auto_scroll(domain):
    for i in range(10):
        command = f"termux-open-url https://www.young.my.id/?q={keyword}&auto_scroll=1"
        print(command)
        system(command)

if __name__ == "__main__":
    keyword = input("Masukkan keyword: ")
    domain = input("Masukkan domain: ")

    open_browser(keyword, domain)
    auto_scroll(domain)
