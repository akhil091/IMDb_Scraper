import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json
import logging

logging.basicConfig(level=logging.INFO)

async def get_movie_details(movie_url, session):
    """
    Extracts movie details from a given IMDb movie page URL asynchronously.
    """
    async with session.get(movie_url) as response:
        page_content = await response.text()
        soup = BeautifulSoup(page_content, 'html.parser')
        title = soup.find('h1').text.strip()
        year = soup.find('span', class_='TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex').text.strip()
        rating = soup.find('span', class_='AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV').text.strip()
        directors = [director.text.strip() for director in soup.find_all('a', class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')]
        cast = [actor.text.strip() for actor in soup.find_all('a', class_='StyledComponents__ActorName-y9ygcu-1 eyqFnv')]
        plot_summary = soup.find('span', class_='GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-2 dcFkRD').text.strip()

        movie_details = {
            'title': title,
            'release_year': year,
            'rating': rating,
            'directors': directors,
            'cast': cast,
            'plot_summary': plot_summary
        }
        return movie_details

async def scrape_movies_by_genre(genre, num_pages):
    """
    Scrapes movie details from IMDb search results for a given genre and specified number of pages asynchronously.
    """
    base_url = 'https://www.imdb.com'
    movie_details_list = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for page in range(1, num_pages + 1):
            url = f'{base_url}/search/title/?genres={genre}&page={page}&ref_=adv_nxt'
            logging.info(f'Scraping page {page}...')
            async with session.get(url) as response:
                page_content = await response.text()
                soup = BeautifulSoup(page_content, 'html.parser')
                search_results = soup.find_all('div', class_='lister-item-content')

                for result in search_results:
                    movie_link = result.find('a', href=True)['href']
                    movie_url = base_url + movie_link
                    tasks.append(get_movie_details(movie_url, session))

        movie_details_list = await asyncio.gather(*tasks)
        
    return movie_details_list

def save_to_json(data, filename):
    """
    Saves scraped data to a JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    genre = input('Enter the genre you want to search for: ')
    num_pages = int(input('Enter the number of pages to scrape: '))
    
    try:
        asyncio.run(scrape_movies_by_genre(genre, num_pages))
        logging.info('Scraping complete.')
    except Exception as e:
        logging.error(f'Error: {e}')
