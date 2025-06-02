from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

url = "http://www.imdb.com/chart/toptv/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url, headers=headers)
print("Status Code: ", response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
script_tag = soup.find("script", id="__NEXT_DATA__")
data = json.loads(script_tag.string)
data_string = data['props']['pageProps']['pageData']['chartTitles']['edges']
rank = 1
tv_show = []

for show in data_string :
    node = show['node']
    title =  node.get('titleText', {}).get('text', 'N/A')
    start_year = node.get('releaseYear', {}).get('year', 'N/A')
    end_year = node.get('releaseYear', {}).get('endYear', 'N/A')
    rating = node.get('ratingsSummary', {}).get('aggregateRating', '0')
    voting_count = node.get('ratingsSummary', {}).get('voteCount', '0')
    genres = [g['genre']['text'] for g in node.get('titleGenres', {}).get('genres', [])]

    tv_show.append({
        'Rank': rank,
        'Title': title,
        'Start Year': str(start_year) if start_year else '',
        'End Year': str(end_year) if end_year else '',
        'Genres': genres,
        'Rating': rating,
        'Vote Count': str(voting_count) if voting_count else ''
    })
    rank+=1

df = pd.DataFrame(tv_show)
df.to_csv('imdb_top_tv_shows.csv', index=False)