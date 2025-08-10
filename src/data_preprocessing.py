def clean_data(data):
    for ticker, df in data.items():
        # Convert index to datetime
        df.index = pd.to_datetime(df.index)
        # Check for missing values
        print(f"Missing values in {ticker}:\n{df.isna().sum()}")
        # Interpolate missing values
        df = df.interpolate(method='linear')
        # Ensure numeric columns
        df = df.astype(float, errors='ignore')
        data[ticker] = df
    return data

if __name__ == "__main__":
    tickers = ['TSLA', 'BND', 'SPY']
    start_date = '2015-07-01'
    end_date = '2025-07-31'
    data = fetch_data(tickers, start_date, end_date)
    data = clean_data(data)
    save_data(data)