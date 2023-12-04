from flask import Flask
from stock_api import get_stock_price

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # When someone visits the home page, this message is displayed
    return 'Hello, World!'

# Define the route for getting stock prices. It uses dynamic URL parameters.
@app.route('/stock/<symbol>')
def stock(symbol):
    # Calls the get_stock_price function from the stock_api module
    # 'symbol' is a variable part of the URL, representing the stock symbol
    stock_price = get_stock_price(symbol)
    # The function returns the stock price, which is then sent back to the client
    return stock_price

# Run the Flask application
# 'debug=True' enables the debugger and auto-reload feature during development
if __name__ == '__main__':
    app.run(debug=True)
