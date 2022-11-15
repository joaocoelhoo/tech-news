from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    search_result = search_news({
        "title": {"$regex": title, "$options": "i"}
    })
    return [(news["title"], news["url"]) for news in search_result]


# Requisito 7
def search_by_date(date):
    try:
        news_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        search_result = search_news({
            "timestamp": {"$regex": news_date}})
        return [(news["title"], news["url"]) for news in search_result]
    except Exception:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    search_tag = search_news({
        "tags": {"$regex": tag, "$options": "i"}
    })
    return [(news["title"], news["url"]) for news in search_tag]


# Requisito 9
def search_by_category(category):
    search_category = search_news({
        "category": {"$regex": category, "$options": "i"}
    })
    return [(news["title"], news["url"]) for news in search_category]
