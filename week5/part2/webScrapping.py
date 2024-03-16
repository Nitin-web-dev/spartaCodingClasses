import requests
from bs4 import BeautifulSoup

# Read the URL and get the HTML,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# You will be scraping the data from this page
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

# Use the requests library to get the HTML code at the url above
data = requests.get(url=url, headers=headers)

# The BeautifulSoup library makes it easy to
# parse HTML code
soup = BeautifulSoup(data.text, 'html.parser')

movie_list = soup.select_one('#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul')


for movie in movie_list:
    single_movie_title = 'div.ipc-metadata-list-summary-item__c > div > div > div.ipc-title.ipc-title--base.ipc-title--title.ipc-title-link-no-icon.ipc-title--on-textPrimary.sc-b0691f29-9.klOwFB.cli-title > a > h3'
    title = movie.select_one(single_movie_title)
    print(title.text)