# Chainlink External Adapter for Stock Prices

## Overview

This project includes a Chainlink External Adapter that allows smart contracts to fetch real-world stock prices, and a Flask-based Stock API. The external adapter serves as a bridge between the Chainlink node and the Stock API, enabling access to stock data from the Twelve Data API.

## Why External Adapters?

External Adapters in Chainlink nodes expand their capabilities, allowing them to retrieve data from external sources. This adapter is crucial for:

- **Data Accessibility**: Providing smart contracts with access to real-world stock price data.
- **Flexibility**: Allowing integration with various data sources and APIs.
- **Security**: Ensuring reliable and secure data transmission.

## Adapter Features

- Retrieves real-time stock prices from the Twelve Data API.
- Easily configurable for various stock symbols.
- Secure API key management.

## Prerequisites

- [Node.js](https://nodejs.org/) and [yarn](https://yarnpkg.com/)
- [Python](https://www.python.org/) and [Poetry](https://python-poetry.org/)
- A [Chainlink Node](https://docs.chain.link/docs/running-a-chainlink-node) (for integration with Chainlink)
- Twelve Data API access

## Setup and Installation

1. **Clone the Repository**
   
   ```bash
   git clone [https://github.com/joshualyguessennd/chainlink_stock_adapter.git]
   ```

2. **Set Up the External Adapter**
   
   Navigate to the `ExternalAdapterProject` directory and install dependencies:
   
   ```bash
   cd ExternalAdapterProject
   yarn install
   ```

   Start the external adapter:
   
   ```bash
   yarn start
   ```

3. **Set Up the Stock API**
   
   Return to the root directory of the repository and install Python dependencies using Poetry:
   
   ```bash
   cd ..
   poetry install
   ```

   Start the Flask Stock API:

   ```bash
   flask run
   ```

   Ensure you have set the required environment variables for the Flask application, including your Twelve Data API key.

4. **Environment Variables**
   
   Create a `.env` file in the Stock API directory with your Twelve Data API key:
   
   ```
   RapidAPIKEY=your_api_key_here
   ```

## Using the Adapter with a Chainlink Node

Configure your Chainlink node to use the external adapter for jobs that require stock price data. Refer to the [Chainlink documentation](https://docs.chain.link/docs/job-specifications/) for creating job specifications.

## Testing

Test the external adapter and Stock API independently using tools like Postman or cURL.

## Contribution

Contributions to this project are welcome. Please submit issues or pull requests on GitHub.

---

This README provides detailed instructions for setting up both the external adapter and the stock API, including the necessary commands and environment setup. Ensure to replace `[repository-url]` with the URL of your actual repository.