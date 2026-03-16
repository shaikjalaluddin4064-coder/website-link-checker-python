import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Website to scan
BASE_URL = "https://www.peugeot.com/en/"

print("Starting link check for:", BASE_URL)

try:
    response = requests.get(BASE_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a")

    print(f"\nTotal links found: {len(links)}\n")

    checked_links = set()

    for link in links:
        href = link.get("href")

        if href:
            full_url = urljoin(BASE_URL, href)

            if full_url not in checked_links:
                checked_links.add(full_url)

                try:
                    r = requests.get(full_url, timeout=5)

                    if r.status_code >= 400:
                        print(f"❌ Broken link: {full_url} | Status: {r.status_code}")
                    else:
                        print(f"✅ Valid link: {full_url} | Status: {r.status_code}")

                except requests.exceptions.RequestException:
                    print(f"⚠️ Error accessing: {full_url}")

except Exception as e:
    print("Error accessing base website:", e)