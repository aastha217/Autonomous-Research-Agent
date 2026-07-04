from app.tools.search import search_web

results = search_web("What are AI agents?")

for result in results:
    print(result["title"])
    print(result["url"])
    print("-" * 50)