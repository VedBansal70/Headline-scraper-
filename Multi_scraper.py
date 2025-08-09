import requests
from bs4 import BeautifulSoup

# Websites to scrape
news_sites = {
    "BBC": "https://www.bbc.com/news",
    "CNN": "https://edition.cnn.com/world",
    "NDTV": "https://www.ndtv.com/latest"
}

all_headlines = []

def scrape_bbc(url):
    headlines = []
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    for item in soup.find_all("h2"):
        text = item.get_text(strip=True)
        if text and len(text) > 10:
            headlines.append(text)
    return headlines

def scrape_cnn(url):
    headlines = []
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    for item in soup.find_all("span", class_="container__headline-text"):
        text = item.get_text(strip=True)
        if text and len(text) > 10:
            headlines.append(text)
    return headlines

def scrape_ndtv(url):
    headlines = []
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    for item in soup.find_all("h2", class_="newsHdng"):
        text = item.get_text(strip=True)
        if text and len(text) > 10:
            headlines.append(text)
    return headlines

# Run scrapers for each site
all_headlines.append(("BBC", scrape_bbc(news_sites["BBC"])));
all_headlines.append(("CNN", scrape_cnn(news_sites["CNN"])));
all_headlines.append(("NDTV", scrape_ndtv(news_sites["NDTV"])));

# Save to file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for site, headlines in all_headlines:
        file.write(f"=== {site} Headlines ===\n")
        for idx, headline in enumerate(headlines, start=1):
            file.write(f"{idx}. {headline}\n")
        file.write("\n")

print("âœ… Scraped headlines from BBC, CNN, and NDTV. Saved to headlines.txt")
