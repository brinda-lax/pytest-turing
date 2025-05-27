'''Task 5:
## Best Listing for Revenue
What is the listing with the best expected revenue based on the last 12 months, 
considering 60% of guests leave reviews and every guest will stay only the minimum number of nights? 

Use both the 'listings' and 'reviews' datasets for this question and only use listings with minimum 
nights of stay <= 7.
 The 'minimum_nights' column indicates the required minimum number of nights of stay for any listing. 
'''

## Find the listing with the best expected revenue over the past 12 months, assuming:

'''60% of guests leave reviews.

Each guest only stays the minimum number of nights.

Use only listings with minimum_nights <= 7.

✅ Columns You'll Use:
From listings:

id: listing ID

## price: price per night (needs cleaning)

## minimum_nights: number of nights per booking

## number_of_reviews_ltm: reviews in last 12 months

## From reviews:
## Not needed directly here, since listings.number_of_reviews_ltm already gives the past 12-month count.'''

import pandas as pd

def revenue(df: pd.DataFrame) -> str:
    dfq_5 = df[['id', 'price', 'minimum_nights', 'number_of_reviews_ltm']].copy()
    dfq_5 = dfq_5[dfq_5['minimum_nights'] <= 7]
    dfq_5['price'] = dfq_5['price'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
    dfq_5 = dfq_5.dropna(subset=['number_of_reviews_ltm', 'price'])
    dfq_5['expected_guests'] = dfq_5['number_of_reviews_ltm'] / 0.6

    dfq_5['Revenue'] = round(dfq_5['price'] * dfq_5['minimum_nights'] * dfq_5['expected_guests'], 2)

    top_listing = dfq_5.loc[dfq_5['Revenue'].idxmax()]

    return f"Listing ID with max expected revenue: {int(top_listing['id'])}, Revenue: ${top_listing['Revenue']:.2f}"


    #revenue=dfq_5.loc[dfq_5['Revenue'].idxmax()]
   # return f"Listing ID with max expected revenue: {int(top_listing['id'])}, Revenue: ${top_listing['Revenue']:.2f}"


if __name__ == "__main__":
    import pandas as pd

    # Load your dataset (adjust path if needed)
    df = pd.read_csv("https://storage.googleapis.com/public-data-337819/listings%202%20reduced.csv", low_memory=False)

    df_2= pd.read_csv("https://storage.googleapis.com/public-data-337819/reviews%202%20reduced.csv", low_memory=False)

    result = revenue(df)
    print(result)