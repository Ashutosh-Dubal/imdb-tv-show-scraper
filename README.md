# 🎬 IMDb Top TV Shows Scraper

This Python project scrapes IMDb's Top Rated TV Shows, extracts key information like title, year, rating, and genres, and saves the data to a CSV file for further analysis or use in other projects. 

## 📚 Table of Contents

- [Why Python for Web Scraping](##-why-python-for-web-scraping)
- [Challenges & Learnings](##-challenges--learnings)
- [How to Install and Run the Project](##-how-to-install-and-run-the-project)
- [How to Use the Project](##-how-to-use-the-project)
- [Sample Output](##-sample-output)
- [Features](##-features)
- [Future Improvements](##-future-improvements)
- [Tech Stack](##-tech-stack)
- [Project Structure](##-project-structure)
- [Author](##-author)
- [License](##-license)

## 🐍 Why Python for Web Scraping?

Python is the industry-standard language for web scraping — and for good reason.

- ✅ **Clean syntax**: Python code is easy to read and write, which makes it ideal for quickly building and adjusting scraping scripts.
- 📦 **Powerful libraries**: Tools like `requests`, `BeautifulSoup`, `Selenium`, and `pandas` make scraping, parsing, and storing data fast and reliable.
- 🌍 **Massive community**: Python has one of the largest developer communities, meaning more tutorials, examples, and help when you need it.
- 🔄 **Integrated data workflow**: With Python, scraped data can be directly passed into data analysis, visualization, or machine learning workflows — no need to switch languages.

Compared to heavier or more verbose languages like Java or C#, Python offers rapid prototyping and a more intuitive developer experience, making it the top choice for scraping and data science projects alike.

## 🧠 Challenges & Learnings

When I first attempted to scrape data from IMDb, I assumed the website was static because all the content appeared immediately in the browser — there was no obvious loading animation or delayed rendering. However, when I sent a simple GET request using Python, I only received partial data — specifically, the top 5 TV shows — instead of the full list.

This made it clear that the page was dynamic and likely rendering data using JavaScript. To work around this, I inspected the page source and discovered that IMDb uses Next.js, which embeds structured JSON data inside a `<script>` tag with the ID `__NEXT_DATA__`. By locating and parsing this tag with BeautifulSoup and `json.loads()`, I was able to access the complete dataset, including all 250 top-rated TV shows, in a clean and structured format.

---
## 🚀 How to Install and Run the Project

Follow these steps to set up and run the IMDb Top TV Shows Scraper:

### 1. Clone the Repository

```bash
git clone https://github.com/Ashutosh-Dubal/imdb-tv-show-scraper.git
cd imdb-tv-show-scraper
```

### 2. (Optional) Create a Virtual Environment

It's recommended to isolate dependencies:

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install all required python packages using pip(on terminal):

```bash
pip install -r requirements.txt
```

If you don't have a requirements.txt, you can generate one with:

```bash
pip freeze > requirements.txt
```

### 4. Run the Script

Run the Scraper:

```bash
python main.py
```

### 5. View the Output

A CSV file named `imdb_top_tv_shows.csv` will be created in your project folder. It contains

- Rank
- Title
- Start & End Year
- IMDb Rating
- Vote Count
- Genres

---

## 📦 How to Use the Project

This script fetches IMDb's Top 250 TV shows using a structured JSON source embedded in the page. It does not require any user input.

Once you run `main.py`, it will:

1. Send an HTTP GET request to IMDb's Top TV chart.
2. Parse and extract relevant data such as:
   - Rank
   - Title
   - Start & End Year
   - Rating
   - Vote Count
   - Genres
3. Save the extracted data into a file named `imdb_top_tv_shows.csv`.

You can open the CSV file with Excel, Google Sheets, or Python to perform further analysis or visualization.

---

## 📊 Sample Output

| Rank | Title         | Start Year | End Year | Rating | Vote Count | Genres                   |
|------|---------------|------------|----------|--------|------------|---------------------------|
| 1    | Breaking Bad  | 2008       | 2013     | 9.5    | 2,337,296  | Crime, Drama, Thriller    |
| 2    | Chernobyl     | 2019       | —        | 9.4    | 911,462    | Drama, History            |

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

## 🔮 Future Improvements

- Add data visualizations (e.g., top 10 by rating or vote count)
- Export data to JSON or SQLite database
- Build a web interface using Flask or Streamlit
- Add unit tests and error handling for robustness

---

## 🧰 Tech Stack

- Python 3
- `requests` – for fetching the IMDb webpage
- `BeautifulSoup` – for parsing HTML to extract embedded JSON
- `json` – to parse the structured data
- `pandas` – to format and export to CSV

----

## 📁 Project Structure

imdb-tv-show-scraper/

├── main.py                  # Scraper script

├── imdb_top_tv_shows.csv    # Output CSV file

├── requirements.txt         # Python dependencies

├── .gitignore

└── README.md

---

## 👨‍💻 Author

Ashutosh Dubal  
🔗 [GitHub Profile](https://github.com/Ashutosh-Dubal)

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
