import requests

# API для получения данных о ценах
COINGECKO_API = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd"

# Пример активов в портфеле
portfolio = {
    "ethereum": 2,
    "bitcoin": 0.5,
    "solana": 10,
    "dogecoin": 1000
}

def get_prices(assets):
    asset_list = ",".join(assets.keys())
    response = requests.get(COINGECKO_API.format(asset_list))
    return response.json()

def calculate_portfolio_value(prices, portfolio):
    total_value = 0
    for asset, amount in portfolio.items():
        if asset in prices:
            total_value += prices[asset]['usd'] * amount
    return total_value

def main():
    prices = get_prices(portfolio)
    total_value = calculate_portfolio_value(prices, portfolio)
    print("Your portfolio value is: ${:.2f}".format(total_value))

if __name__ == "__main__":
    main()
