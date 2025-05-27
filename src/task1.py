import pandas as pd

print("Script is running")


def neighborhood_with_biggest_price_diff(df: pd.DataFrame) -> str:
    # Select and clean data
    df_super_host = df[['host_is_superhost', 'neighbourhood_cleansed', 'price']].copy()
    df_super_host['price'] = (
        df_super_host['price']
        .str.replace('$', '', regex=False)
        .str.replace(',', '', regex=False)
        .astype(float)
    )

    # Compute median prices
    median_prices = (
        df_super_host
        .groupby(['host_is_superhost', 'neighbourhood_cleansed'])['price']
        .median()
        .dropna()
        .reset_index()
    )

    # Split into superhost and non-superhost medians
    median_f = median_prices[median_prices['host_is_superhost'] == 'f'].rename(columns={'price': 'non_superhost_median'})
    median_t = median_prices[median_prices['host_is_superhost'] == 't'].rename(columns={'price': 'superhost_median'})

    # Merge on neighborhood
    merged = pd.merge(median_t, median_f, on='neighbourhood_cleansed')

    # Compute absolute price difference
    merged['price_diff'] = (merged['superhost_median'] - merged['non_superhost_median']).abs()

    # Get neighborhood with max difference
    result = merged.sort_values(by='price_diff', ascending=False).iloc[0]

    return result['neighbourhood_cleansed']
if __name__ == "__main__":
    import pandas as pd

    # Load your dataset (adjust path if needed)
    df = pd.read_csv("https://storage.googleapis.com/public-data-337819/listings%202%20reduced.csv", low_memory=False)

    # Call the function and print result
    result = neighborhood_with_biggest_price_diff(df)
    print("Neighborhood with biggest median price difference:", result)