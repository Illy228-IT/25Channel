import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}


def get_news_from_sources(sources):

    results = []

    for url in sources:

        try:

            response = requests.get(
                url,
                headers=HEADERS,
                timeout=15
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            # Удаляем мусор сайта
            for tag in soup([
                "script",
                "style",
                "header",
                "footer",
                "nav",
                "aside",
                "form"
            ]):
                tag.decompose()

            title = ""

            if soup.title:
                title = soup.title.get_text(strip=True)

            paragraphs = []

            # Берём только текст абзацев
            for p in soup.find_all("p"):

                text = p.get_text(
                    separator=" ",
                    strip=True
                )

                if len(text) > 50:
                    paragraphs.append(text)

            article_text = "\n".join(paragraphs)

            # Ограничиваем размер
            article_text = article_text[:4000]

            results.append(
                f"""
Источник:
{url}

Заголовок:
{title}

Содержимое статьи:
{article_text}
"""
            )

        except Exception as e:

            print(
                f"Ошибка источника {url}: {e}"
            )

    return "\n\n".join(results)