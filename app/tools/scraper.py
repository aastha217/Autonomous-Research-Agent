import requests
from bs4 import BeautifulSoup


def scrape_article(url: str):
    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        paragraphs = soup.find_all("p")

        text = "\n".join(
            p.get_text(strip=True)
            for p in paragraphs
        )

        return text

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""