import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from newspaper import Article

def scrape_website_list(): #scrapes the first 10 pages of HackerNews
    mega_links, mega_subtext, mega_ages = [], [], []

    for i in range(1, 100):
        res = requests.get(f'https://news.ycombinator.com/news?p={i}')
        soup = BeautifulSoup(res.text, 'html.parser')

        links = soup.select('.titleline > a')
        ages = soup.select('.age > a')
        subtext = soup.select('.subtext')
        mega_links.extend(links)
        mega_subtext.extend(subtext)
        mega_ages.extend(ages)

    return mega_links, mega_subtext, mega_ages

'''def scrape_news_sources(hn: list):
    article_html = []

    op = webdriver.FirefoxOptions()
    op.add_argument("-headless")
    driver = webdriver.Firefox(options=op)
    for article in hn:
        driver.get(article['link'])
        req_soup = BeautifulSoup(driver.page_source, 'html.parser')
        clean_text = clean_html(req_soup)
        article_html.append(clean_text)
    driver.close()
    return article_html'''

def scrape_news_sources(hn: list):
    article_summaries=[]

    for art in hn:
        article = Article(art['link'])
        article.download()
        try:
            article.parse()
        except Exception as e:
            article_summaries.append("Could not be summarized due to captcha error, you can read the full article below.")
            continue
        article.nlp()
        article_summaries.append(article.summary)

    return article_summaries

def clean_html(soup: BeautifulSoup):
    raw = soup.getText()
    raw = re.sub(r'\s+', ' ', raw).strip()
    return raw
