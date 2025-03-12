from feedgen.feed import FeedGenerator
import os

# Create RSS feed object
fg = FeedGenerator()
fg.id("https://ttwiz.github.io/substack-rss/")
fg.title("My Blog RSS")
fg.author({'name': 'TTWiz', 'email': 'alan@porthouse.me.uk'})
fg.link(href="https://ttwiz.github.io/substack-rss/rss.xml", rel="self")
fg.language("en")
fg.description("Migrated blog posts from WordPress")

# Read extracted posts and add them to the feed
for file in os.listdir("."):
    if file.endswith(".md"):  # Assuming posts are in Markdown format
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        fe
