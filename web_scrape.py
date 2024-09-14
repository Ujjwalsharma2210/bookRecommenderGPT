from bs4 import BeautifulSoup
import requests

url = "https://blog.reedsy.com/book-genres"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def getGenres():
    genresList = []
    genreMeaniingList = []

    page_to_scrape = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(page_to_scrape.text, "html.parser")

    genres = soup.find_all("h3")
    explainations = soup.find_all("p")

    # for explaination in explainations:
    #     print(explaination.text, end="\n")

    for genre in genres:
        genresList.append(genre.text)

    print(genresList)

getGenres()