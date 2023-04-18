#!/usr/bin/env python3
import newspaper
import os

path = os.getcwd()
print(path)

if not os.path.exists('/tmp/.newspaper_scraper'):
    origem = os.path.join(path,'newspaper_scraper')
    print(origem)
    os.symlink(origem,'/tmp/.newspaper_scraper/')

url = 'https://www.jn.pt'


jn = newspaper.build(url)

print(jn.size())

for article in jn.articles:
    #print(article.url,article.title)
    ar = newspaper.Article(article.url)
    ar.download()
    ar.parse()
    print(f'''
<article>
    <title>{ar.title}</title>
    <url>{ar.url}</url>
    <autor>{ar.authors}</autor>
    <date>{ar.publish_date}</date>
    <text>{ar.text}</text>
</article>
    ''')