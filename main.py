import requests
import feedparser
import os
from datetime import datetime
import html

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_USER_ID = os.getenv("TG_USER_ID")
KEYWORDS = ["习近平", "習近平", "Xi Jinping"]

NEWS_SOURCES = [
    "https://news.google.com/rss/search?q=Xi+Jinping&hl=en-US&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=习近平&hl=zh-CN&gl=CN&ceid=CN:zh",
    "https://www.rfa.org/mandarin/rss2.xml",
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://www.voachinese.com/api/zrqite$eim",
    "https://www.dw.com/zh/zh-%E6%96%B0%E9%97%BB/s-2654?maca=zh-rss-zh-all-1131-rdf"
]

def send_telegram_message(text):
    if not TG_BOT_TOKEN or not TG_USER_ID:
        print("Token or User ID not set")
        return
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TG_USER_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    try:
        requests.post(url, data=payload, timeout=10)
    except Exception as e:
        print("Error sending Telegram message:", e)

def check_feeds():
    for url in NEWS_SOURCES:
        feed = feedparser.parse(url)
        for entry in feed.entries[:10]:
            title = html.unescape(entry.title)
            summary = html.unescape(entry.get("summary", ""))
            link = entry.link
            if any(kw in title + summary for kw in KEYWORDS):
                pub_time = entry.get("published", "") or datetime.utcnow().strftime("%Y-%m-%d %H:%M")
                message = f"📢 <b>{title}</b>\n📰 来源: {url.split('/')[2]}\n🕒 时间: {pub_time}\n🔗 链接: {link}"
                send_telegram_message(message)

if __name__ == "__main__":
    check_feeds()