from app.tools.scraper import scrape_article

url = "https://www.ibm.com/think/topics/ai-agents"

content = scrape_article(url)

print(content[:2000])