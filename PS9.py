import json
from collections import defaultdict

with open('ps9.json', 'r') as file:
    data = json.load(file)

article_views = defaultdict(int)

for month_data in data:
    for article, views in month_data.items():
        article_views[article] += views


def sort_articles(article):
    return (-article[1], article[0])

sorted_articles = sorted(article_views.items(), key=sort_articles)

for i, (article, views) in enumerate(sorted_articles[:1000], 1):
    print(i, "Article:", article , "Views:" ,views)

 