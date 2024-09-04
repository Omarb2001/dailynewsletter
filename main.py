from bs4 import BeautifulSoup
import re
from scraper import scrape_website_list, scrape_news_sources
from summarize import compilation
from email_handler import messenger

#section 1: tech news


def sort_stories_by_votes(hnlist): #sorts hn list in reverse order
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext, ages): #takes scraped data and makes a list of articles with more than 500 votes
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        age_of_article = ages[idx].getText()
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99 and 'https' in href and 'github' not in href and 'day' not in age_of_article: #making sure it's only articles
                hn.append({'title': title, 'link': href, 'votes': points, 'age': age_of_article})
    return sort_stories_by_votes(hn)

def filter_out_top_10(hn: list): #only takes top 10 articles to prevent making the newsletter too long
    if len(hn)<10:
        return hn
    return hn[:10]



def clean_html(soup: BeautifulSoup):
    raw = soup.getText()
    raw = re.sub(r'\s+', ' ', raw).strip()


def main():
    mega_links, mega_subtext, mega_ages = scrape_website_list()

    stories = filter_out_top_10(create_custom_hn(mega_links, mega_subtext, mega_ages))

    summaries = scrape_news_sources(stories)
    stories = compilation(summaries, stories)

    messenger(stories)



if __name__ == '__main__':
    main()
#Political news (world)
#political news(Jordan)
#Stocks/economic news