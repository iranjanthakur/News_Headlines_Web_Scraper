import requests
from bs4 import BeautifulSoup
import time

def scrape_news_headlines(url, output_file="headlines.txt"):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        headlines = []
        for tag in ['h1', 'h2', 'h3']:
            for element in soup.find_all(tag):
                text = element.get_text(strip=True)
                if text and len(text) > 10:
                    headlines.append(text)

        seen = set()
        unique_headlines = []
        for headline in headlines:
            if headline not in seen:
                unique_headlines.append(headline)
                seen.add(headline)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"Scraped from: {url}\n")
            file.write(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("=" * 60 + "\n\n")
            for i, h in enumerate(unique_headlines[:20], 1):
                file.write(f"{i}. {h}\n")

        print("\nTop Headlines:\n" + "-" * 50)
        for i, h in enumerate(unique_headlines[:20], 1):
            print(f"{i}. {h}")
        
        print(f"\nSaved to '{output_file}'.")

    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print("=== News Headlines Scraper ===")

    news_sites = [
        "https://www.bbc.com/news",
        "https://news.ycombinator.com",
        "https://www.reuters.com"
    ]

    for i, site in enumerate(news_sites, 1):
        print(f"{i}. {site}")

    choice = input("\nChoose a site number (or press Enter for default): ").strip()
    url = news_sites[0]

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(news_sites):
            url = news_sites[index]

    custom = input("Enter custom URL (or press Enter to skip): ").strip()
    if custom:
        url = custom

    scrape_news_headlines(url)

if __name__ == "__main__":
    main()
