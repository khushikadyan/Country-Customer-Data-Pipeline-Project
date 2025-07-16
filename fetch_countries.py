import requests
import json
import os
from datetime import datetime

def fetch_country_data():
    countries = ['india', 'us', 'uk', 'china', 'russia']
    url_template = "https://restcountries.com/v3.1/name/{name}"
    
    
    os.makedirs("country_data", exist_ok=True)
    
    for country in countries:
        try:
            response = requests.get(url_template.format(name=country), timeout=10)
            if response.status_code == 200:
                data = response.json()
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"country_data/{country.lower()}_{timestamp}.json"
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                print(f" Saved data for {country} at {timestamp}")
            else:
                print(f" Failed to fetch {country} (HTTP {response.status_code})")
        except Exception as e:
            print(f"⚠️ Error fetching {country}: {str(e)}")

if __name__ == "__main__":
    fetch_country_data()  