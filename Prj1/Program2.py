import requests

API_KEY = 'XXX'

URL_TO_SCRAPE = 'https://www.leboncoin.fr'

payload = {'api_key': API_KEY, 'url': URL_TO_SCRAPE, 'render': 'true'}

r = requests.get('http://api.scraperapi.com', params=payload, timeout=60)

print(r.status_code)

html = r.text.strip()