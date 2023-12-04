import os
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file located in the same directory as this script.
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

def get_stock_price(symbol):
    """
    Fetches the current stock price for a given symbol using the Twelve Data API.

    :param symbol: The stock symbol for which the price needs to be fetched.
    :return: A dictionary containing the symbol and its current price.
    """
    # URL of the Twelve Data API endpoint for fetching stock prices.
    url = "https://twelve-data1.p.rapidapi.com/price"

    # Parameters for the API request, including the stock symbol and response format.
    querystring = {"symbol": symbol, "format": "json", "outputsize": "30"}

    # Headers for the API request, including the API key read from the environment variable.
    headers = {
        "X-RapidAPI-Key": os.getenv('RapidAPIKEY'),  # API key is stored in an environment variable for security.
        "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
    }

    # Sending a GET request to the API and storing the response.
    response = requests.get(url, headers=headers, params=querystring)
    response_data = response.json()

    # Extracting the price from the response. Defaults to 'Unavailable' if the price key is not found.
    price = response_data.get('price', 'Unavailable')

    # Returning the stock symbol and its price as a dictionary.
    return {"data": {"symbol": symbol, "price": price}}
