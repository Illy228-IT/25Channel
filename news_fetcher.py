import feedparser


def _get_news(url):

    try:

        feed = feedparser.parse(url)

        if feed.entries:

            return f"""
Заголовок:
{feed.entries[0].title}

Описание:
{feed.entries[0].summary}
"""

        return "Нет новостей"

    except Exception as e:

        return f"Ошибка получения новости: {e}"


def get_crypto_news():
    return _get_news(
        "https://cointelegraph.com/rss"
    )


def get_ai_news():
    return _get_news(
        "https://www.artificialintelligence-news.com/feed/"
    )


def get_world_news():
    return _get_news(
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
    )


def get_sport_news():
    return _get_news(
        "https://www.espn.com/espn/rss/news"
    )


def get_europe_news():
    return get_world_news()


def get_america_news():
    return get_world_news()


def get_ukraine_news():
    return get_world_news()


def get_travel_news():
    return get_world_news()


def get_jobs_news():
    return get_world_news()


def get_real_estate_news():
    return get_world_news()


def get_advertising_news():
    return get_world_news()


def get_marketplace_news():
    return get_world_news()


def get_beauty_news():
    return get_world_news()


def get_prague_news():
    return get_world_news()


def get_friends_news():
    return get_world_news()


def get_search_news():
    return get_world_news()


def get_services_news():
    return get_world_news()


def get_auto_news():
    return get_world_news()