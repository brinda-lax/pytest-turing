'''Task 7: Second strongest correlated host attribute with number of reviews
Which host attribute has the second-strongest correlation with the number of reviews of the listing?
 Use the following columns as the host attributes: 'host_since', 'host_listings_count', 'host_identity_verified', 
 'calculated_host_listings_count', 'host_is_superhost', Use 'number_of_reviews' as the column to find correlation with. 
 [Difficulty: Medium]'''

import pandas as pd
def type_of_host(df: pd.DataFrame) -> str:
    dfq_7=df[['host_since','host_listings_count','calculated_host_listings_count','host_identity_verified','host_is_superhost','number_of_reviews']].copy()

    dfq_7['host_since']=pd.to_datetime(dfq_7['host_since'],errors='coerce')
    dfq_7['hosted_year']=dfq_7['host_since'].dt.year

    dfq_7.head()
    dfq_7['host_identity_verified']=dfq_7['host_identity_verified'].map({'t':1,'f':0})
    dfq_7['host_is_superhost']=dfq_7['host_is_superhost'].map({'t':1,'f':0})

    correl_df7=dfq_7.corr()['number_of_reviews'].drop('number_of_reviews').abs().sort_values(ascending=False).reset_index(name='Correlation_value')

    correl_df7.rename(columns={'index':'Column_name'},inplace=True)
    result=correl_df7.iloc[1,0]
    return f" Second strongest correlated host attribute with number of reviews is {result.upper()}"
if __name__ == "__main__":
    import pandas as pd

    # Load your dataset (adjust path if needed)
    df = pd.read_csv("https://storage.googleapis.com/public-data-337819/listings%202%20reduced.csv", low_memory=False)

    # Call the funcstion and print result
    type_of_host(df)
    print(type_of_host(df))