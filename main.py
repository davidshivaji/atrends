import sys
from atrends.config import DEFAULT_TIMEFRAME, DEFAULT_CATEGORY, DEFAULT_GEO
from atrends.data_fetcher import GoogleTrendsFetcher
from atrends.plotter import plot_interest_over_time

def main(keywords):
    if not keywords:
        print("Please provide at least one keyword.")
        return

    fetcher = GoogleTrendsFetcher()
    data = fetcher.fetch_with_retries(keywords, timeframe=DEFAULT_TIMEFRAME, geo=DEFAULT_GEO, category=DEFAULT_CATEGORY)

    if data is None or data.empty:
        print("Failed to fetch data from Google Trends. Please try again later or with different keywords.")
        return

    plot_interest_over_time(data, keywords)

if __name__ == "__main__":
    all_keywords = sys.argv[1:]
    main(all_keywords)
