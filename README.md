## IMDb_Scraper
Python web scraper that extracts movie information from IMDb.
Used the "Beautiful Soup" library for parsing HTML and the "Requests" library for making HTTP requests.
Scraper uses asynchronous programming with 'asyncio' and 'aiohttp' to improve performance by making multiple HTTP requests concurrently. Error handling is implemented to catch and log any exceptions that may occur during the scraping process. Pagination handling is done asynchronously as well.

This scraper allows you to specify a genre and the number of pages you want to scrape. It scrapes movie details such as title, year, rating, directors, cast, and plot summary from IMDb search results. It then saves the scraped data to a JSON file named movies.json.


### To run the scraper, follow these steps:

#### 1. Install Python:
If you don't have Python installed on your system, download and install it from the official Python website: https://www.python.org/downloads/

#### 2. Install dependencies:
Open a terminal or command prompt, navigate to the directory containing the scraper script, and install the required dependencies using pip:
```cmd
pip install requests beautifulsoup4
```
#### 3. Run the scraper:
Open a terminal or command prompt, navigate to the directory containing the imdb_scraper.py file, and execute the script by running the following command:
```
python imdb_scraper.py
```
#### 4. Follow the prompts:
The script will prompt you to enter the genre you want to search for and the number of pages you want to scrape. Enter the desired values when prompted.

#### 5. Wait for scraping to complete:
The scraper will start scraping movie details from IMDb based on your inputs. It will display progress messages as it progresses through each page. Once scraping is complete, it will save the extracted data to a JSON file named movies.json in the same directory.

#### 6. Check the output:
After the scraping is complete, you can check the movies.json file to view the extracted movie details.

That's it! You have successfully run the IMDb scraper and extracted movie information based on your chosen genre and number of pages.
