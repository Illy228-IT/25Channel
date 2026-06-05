import asyncio
import time
import schedule

from telegram_publisher import start_client, publish
from openai_client import generate_post
from source_fetcher import get_news_from_sources
from openai_client import generate_news_post

from channels.channel_friends import CHANNEL as FRIENDS_CHANNEL, PROMPT as FRIENDS_PROMPT
#from channels.channel_job_eu import CHANNEL as JOB_EU_CHANNEL, PROMPT as JOB_EU_PROMPT
#from channels.channel_market import CHANNEL as MARKET_CHANNEL, PROMPT as MARKET_PROMPT
from channels.channel_network import CHANNEL as NETWORK_CHANNEL, PROMPT as NETWORK_PROMPT
from channels.channel_services import CHANNEL as SERVICES_CHANNEL, PROMPT as SERVICES_PROMPT

from channels.channel_ai import (
    CHANNEL as AI_CHANNEL,
    PROMPT as AI_PROMPT,
    SOURCES as AI_SOURCES
)

from channels.channel_america import (
    CHANNEL as AMERICA_CHANNEL,
    PROMPT as AMERICA_PROMPT,
    SOURCES as AMERICA_SOURCES
)

from channels.channel_auto import (
    CHANNEL as AUTO_CHANNEL,
    PROMPT as AUTO_PROMPT,
    SOURCES as AUTO_SOURCES
)

#from channels.channel_beauty import (
    #PROMPT as BEAUTY_PROMPT,
    #)

#from channels.channel_europa_job import (
    #CHANNEL as EUROPA_JOB_CHANNEL,
    #PROMPT as EUROPA_JOB_PROMPT,
    #SOURCES as EUROPA_JOB_SOURCES
#)

#from channels.channel_extra import (
    #CHANNEL as EXTRA_CHANNEL,
    #PROMPT as EXTRA_PROMPT,
    #SOURCES as EXTRA_SOURCES
#)

from channels.channel_fm import (
    CHANNEL as FM_CHANNEL,
    PROMPT as FM_PROMPT,
    SOURCES as FM_SOURCES
)

from channels.channel_future import (
    CHANNEL as FUTURE_CHANNEL,
    PROMPT as FUTURE_PROMPT,
    SOURCES as FUTURE_SOURCES
)

#from channels.channel_info import (
    #CHANNEL as INFO_CHANNEL,
    #PROMPT as INFO_PROMPT,
    #SOURCES as INFO_SOURCES
#)

from channels.channel_news import (
    CHANNEL as NEWS_CHANNEL,
    PROMPT as NEWS_PROMPT,
    SOURCES as NEWS_SOURCES
)

#from channels.channel_prague_job import (
    #CHANNEL as PRAGUE_JOB_CHANNEL,
    #PROMPT as PRAGUE_JOB_PROMPT,
    #SOURCES as PRAGUE_JOB_SOURCES
#)

#from channels.channel_real_estate import (
    #CHANNEL as REAL_ESTATE_CHANNEL,
    #PROMPT as REAL_ESTATE_PROMPT,
    #SOURCES as REAL_ESTATE_SOURCES
#)

#from channels.channel_search import (
    ##CHANNEL as SEARCH_CHANNEL,
    #PROMPT as SEARCH_PROMPT,
    #SOURCES as SEARCH_SOURCES
#)

from channels.channel_sport import (
    CHANNEL as SPORT_CHANNEL,
    PROMPT as SPORT_PROMPT,
    SOURCES as SPORT_SOURCES
)

from channels.channel_travel import (
    CHANNEL as TRAVEL_CHANNEL,
    PROMPT as TRAVEL_PROMPT,
    SOURCES as TRAVEL_SOURCES
)

from channels.channel_ukraine import (
    CHANNEL as UKRAINE_CHANNEL,
    PROMPT as UKRAINE_PROMPT,
    SOURCES as UKRAINE_SOURCES
)

from channels.channel_weapon import (
    CHANNEL as WEAPON_CHANNEL,
    PROMPT as WEAPON_PROMPT,
    SOURCES as WEAPON_SOURCES
)

#from channels.channel_work_eu import (
    #CHANNEL as WORK_EU_CHANNEL,
    #PROMPT as WORK_EU_PROMPT,
    #SOURCES as WORK_EU_SOURCES
#)

from channels.channel_world import (
    CHANNEL as WORLD_CHANNEL,
    PROMPT as WORLD_PROMPT,
    SOURCES as WORLD_SOURCES
)

#from channels.channel_ads import (
    #CHANNEL as ADS_CHANNEL,
    #PROMPT as ADS_PROMPT,
    #SOURCES as ADS_SOURCES
#)

async def publish_all():

    await start_client()

    news_channels = [

        (AI_CHANNEL, AI_PROMPT, AI_SOURCES),
        (AMERICA_CHANNEL, AMERICA_PROMPT, AMERICA_SOURCES),
        (AUTO_CHANNEL, AUTO_PROMPT, AUTO_SOURCES),
        #(BEAUTY_CHANNEL, BEAUTY_PROMPT, BEAUTY_SOURCES),
        #(EUROPA_JOB_CHANNEL, EUROPA_JOB_PROMPT, EUROPA_JOB_SOURCES),
        #(EXTRA_CHANNEL, EXTRA_PROMPT, EXTRA_SOURCES),
        (FM_CHANNEL, FM_PROMPT, FM_SOURCES),
        (FUTURE_CHANNEL, FUTURE_PROMPT, FUTURE_SOURCES),
        #(INFO_CHANNEL, INFO_PROMPT, INFO_SOURCES),
        (NEWS_CHANNEL, NEWS_PROMPT, NEWS_SOURCES),
        #(PRAGUE_JOB_CHANNEL, PRAGUE_JOB_PROMPT, PRAGUE_JOB_SOURCES),
        #(REAL_ESTATE_CHANNEL, REAL_ESTATE_PROMPT, REAL_ESTATE_SOURCES),
        #(SEARCH_CHANNEL, SEARCH_PROMPT, SEARCH_SOURCES),
        (SPORT_CHANNEL, SPORT_PROMPT, SPORT_SOURCES),
        (TRAVEL_CHANNEL, TRAVEL_PROMPT, TRAVEL_SOURCES),
        (UKRAINE_CHANNEL, UKRAINE_PROMPT, UKRAINE_SOURCES),
        (WEAPON_CHANNEL, WEAPON_PROMPT, WEAPON_SOURCES),
        #(WORK_EU_CHANNEL, WORK_EU_PROMPT, WORK_EU_SOURCES),
        (WORLD_CHANNEL, WORLD_PROMPT, WORLD_SOURCES),
        #(ADS_CHANNEL, ADS_PROMPT, ADS_SOURCES),
    ]

    static_channels = [

        (FRIENDS_CHANNEL, FRIENDS_PROMPT),
        #(JOB_EU_CHANNEL, JOB_EU_PROMPT),
        #WORK_CHANNEL, NETWORK_PROMPT),
        (SERVICES_CHANNEL, SERVICES_PROMPT),

    ]

    for channel, prompt, sources in news_channels:

        try:

            print(f"\nПубликую новость в {channel}")

            news = get_news_from_sources(
                sources
            )

            text = generate_news_post(
                prompt,
                news
            )

            await publish(
                channel,
                text
            )

            print(f"Успешно: {channel}")

            await asyncio.sleep(20)

        except Exception as e:

            print(f"Ошибка {channel}: {e}")

    for channel, prompt in static_channels:

        try:

            print(f"\nПубликую пост в {channel}")

            text = generate_post(
                prompt
            )

            await publish(
                channel,
                text
            )

            print(f"Успешно: {channel}")

            await asyncio.sleep(20)

        except Exception as e:

            print(f"Ошибка {channel}: {e}")

def run_cycle():

    print("\n======================")
    print("НОВЫЙ ЦИКЛ ПУБЛИКАЦИИ")
    print("======================\n")

    asyncio.run(
        publish_all()
    )


schedule.every(3).hours.do(run_cycle)

print("Бот запущен")
print("Публикация каждые 3 часа")

run_cycle()

while True:

    schedule.run_pending()

    time.sleep(10)