import pandas as pd

print("Script is running")
def strongest(df: pd.DataFrame) -> str:
    dfq_2=df[['price','review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 'review_scores_value']]
    dfq_2.loc[:,'price']=(dfq_2['price'].str.replace('$','',regex=False).str.replace(',','',regex=False).astype(float))
    correl=dfq_2.corr()['price'].drop('price')
    strongest = correl.abs().idxmax()
    
    return f"The Strongest correlation column with Price is {strongest} and its value is {correl[strongest]}"


if __name__ == "__main__":
    import pandas as pd

    # Load your dataset (adjust path if needed)
    df = pd.read_csv("https://storage.googleapis.com/public-data-337819/listings%202%20reduced.csv", low_memory=False)

    # Call the function and print result
    result = strongest(df)
    print(result)