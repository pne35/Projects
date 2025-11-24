import requests
from bs4 import BeautifulSoup
import time

# Headers to mimic a browser (to avoid being blocked)
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

# Function to fetch price data
def get_price(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the price on the page (depends on Amazon's structure)
    price = soup.select_one('.a-price .a-offscreen')
    if price:
        return str(price.text.replace('$', '').replace(',', '').strip())
    return None

# Watchlist
watchlist = {
    'Koorui Monitor': 'https://www.amazon.co.uk/KOORUI-Compatible-Adjustable-Mountable-DisplayPort/dp/B0B6B1RDKB/ref=asc_df_B0B6B1RDKB?mcid=d777f44019673319bfe3696a50dae2f9&th=1&hvocijid=5606422366779031013-B0B6B1RDKB-&hvexpln=74&tag=googshopuk-21&linkCode=df0&hvadid=696285193871&hvpos=&hvnetw=g&hvrand=5606422366779031013&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9046582&hvtargid=pla-2281435177138&gad_source=1',  # Replace with your product URL
}

# Track price changes
def track_prices():
    price_data = {}
    for item, url in watchlist.items():
        price = get_price(url)
        if price is not None:
            price_data[item] = price
    return price_data

# Main loop
if __name__ == '__main__':
    tracked_prices = {}
    print("Starting price tracker...")

    while True:
        current_prices = track_prices()

        # Compare with previous prices
        for item, price in current_prices.items():
            if item in tracked_prices:
                old_price = tracked_prices[item]
                if price < old_price:
                    print(f'Price Drop Alert! {item}: Old Price: £{old_price}, New Price: £{price}')
                elif price > old_price:
                    print(f'Price Increase Alert! {item}: Old Price: £{old_price}, New Price: £{price}')
                else:
                    print(f'Price Stayed The Same! {item}: Old Price: £{old_price}, New Price: £{price}')
            else:
                print(f'New Item Tracked: {item} at £{price}')
        
        tracked_prices.update(current_prices)

        # Wait before next check (e.g., every hour)
        time.sleep(5)
