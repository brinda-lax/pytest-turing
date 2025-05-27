import pandas as pd

def neighbor_avg_price(df: pd.DataFrame) -> str:
    dfq_3=df[['host_id','neighbourhood_cleansed','price']].copy()
    dfq_3['price']=(dfq_3['price'].str.replace('$','',regex=False).str.replace(',','',regex=False).astype(float))
    high_neigh_count=dfq_3.groupby('host_id')['neighbourhood_cleansed'].nunique().reset_index(name='unique_neigh_count')
    high_neigh_count['is_professional'] = high_neigh_count['unique_neigh_count'] > 5
    merged_neigh=pd.merge(dfq_3,high_neigh_count[['host_id', 'is_professional']],on='host_id')

    average_price=merged_neigh.groupby('is_professional')['price'].mean().reset_index(name='avg_price')

    non_professional=average_price.loc[average_price['is_professional']==False,'avg_price'].values[0]

    professional=average_price.loc[average_price['is_professional']==True,'avg_price'].values[0]

    diff=professional-non_professional

    return f"The Average difference in price of professional and non professional is {diff}"


if __name__ == "__main__":
    import pandas as pd
    print("Script is running")

    # Load your dataset (adjust path if needed)
    df = pd.read_csv("https://storage.googleapis.com/public-data-337819/listings%202%20reduced.csv", low_memory=False)

    result = neighbor_avg_price(df)
    print(result)

