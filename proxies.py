import requests
import random

scrape_url = "https://www.tripadvisor.in/Attraction_Review-g297685-d319858-Reviews-Ganges_River-Varanasi_Varanasi_District_Uttar_Pradesh.html"


# Load proxies from file
with open('proxies.txt', 'r') as file:
    proxy_list = file.read().splitlines()

def scrape_with_proxy(url):
    # Choose a random proxy from the list
    proxy = random.choice(proxy_list)
    proxy_dict = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }

    try:
        response = requests.get(url, proxies=proxy_dict, timeout=5)
        # Handle the response
        print(response.text)
    except Exception as e:
        print(f"Error occurred: {e}")

scrape_with_proxy(scrape_url)
