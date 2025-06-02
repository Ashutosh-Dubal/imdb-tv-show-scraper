# 🎬 IMDb Top TV Shows Scraper

This Python project scrapes IMDb's Top Rated TV Shows, extracts key information like title, year, rating, and genres, and saves the data to a CSV file for further analysis or use in other projects.

---

## 📌 Features

- Scrapes data directly from IMDb’s internal JSON
- Extracts:
  - Rank
  - Title
  - Start & End Year
  - IMDb Rating
  - Vote Count
  - Genres
- Saves data into `imdb_top_tv_shows.csv`

---

## 🧰 Tech Stack

- Python 3
- `requests` – for fetching the IMDb webpage
- `BeautifulSoup` – for parsing HTML to extract embedded JSON
- `json` – to parse the structured data
- `pandas` – to format and export to CSV
