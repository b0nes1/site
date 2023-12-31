import feedparser
import random

def get_news():
    NewsFeed = feedparser.parse("https://feeds.skynews.com/feeds/rss/world.xml")
    stories = []
    for entry in NewsFeed.get("entries"):
        stories.append((entry.get("title")+ ". ", entry.get("links")[0].get("href")))
        random.shuffle(stories)
    return stories