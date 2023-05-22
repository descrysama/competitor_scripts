import requests

def fetch_items():
    url = "http://79.137.87.52:5000/sku/get"

    try:
        response = requests.get(url)
        response.raise_for_status() 
        items = response.json()
        return items
    except requests.exceptions.RequestException as e:
        print("Error occurred during request:", e)
        return []