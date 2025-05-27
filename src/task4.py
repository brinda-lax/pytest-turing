'''Task 4: Median Price Premium
What is the median price premium given to entire homes / 
entire apartments with respect to other listings of the same neighborhood? 
Report the average across all neighborhoods.
Use the 'room_type' column in the 'listings'
 dataset to distinguish between entire homes / entire apartments and other types of listings.'''

import pandas as pd

print("Script is running")
def strongest(df: pd.DataFrame) -> str:
    dfq_4=df[['price','room_type','neighbourhood_cleansed']].copy()
    #dfq_4['room_type'].value_counts()
    dfq_4['price']=dfq_4['price'].str.replace('$','',regex=False).str.replace(',','',regex=False).astype(float)
    pivoted = dfq_4.pivot_table(
    index='neighbourhood_cleansed',
    columns='room_type',
    values='price',
    aggfunc='median'  # or 'mean'
    ).reset_index()
    pivoted.fillna(0,inplace=True)
    if 'Entire home/apt' not in pivoted.columns:
        return "No 'Entire home/apt' listings found in the data."
    else:
        other_columns = [col for col in pivoted.columns if col not in ['neighbourhood_cleansed', 'Entire home/apt']]
        pivoted['other_median'] = pivoted[other_columns].mean(axis=1, skipna=True)
        pivoted['premium'] = pivoted['Entire home/apt'] - pivoted['other_median']

        return f"Average premium: {pivoted['premium'].mean():.2f}"

if __name__ == "__main__":
    import pandas as pd

    # Load your dataset (adjust path if needed)
    df = pd.read_csv("https://storage.googleapis.com/public-data-337819/listings%202%20reduced.csv", low_memory=False)

    # Call the funcstion and print result
    strongest(df)
    print(strongest(df))