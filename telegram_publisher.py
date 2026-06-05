from telethon import TelegramClient
from config import API_ID, API_HASH

client = TelegramClient(
    "session",
    API_ID,
    API_HASH
)


async def start_client():
    await client.start()


async def publish(channel, text):
    await client.send_message(
        entity=channel,
        message=text,
        parse_mode="html"
    )