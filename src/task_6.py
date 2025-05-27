import pandas as pd

def average_review_difference(df: pd.DataFrame) -> str:
    # Filter out listings with null review scores
    dfq_6 = df[df['review_scores_rating'].notnull()]
    
    # Calculate average review score by host type
    avg_scores = dfq_6.groupby('host_is_superhost')['review_scores_rating'].mean().reset_index(name='Average_review')

    # Handle cases where either superhost or non-superhost is missing
    if avg_scores.shape[0] < 2:
        return "Insufficient data to compare superhosts and normal hosts."

    # Calculate the difference between superhost and normal host average review score
    diff_avg = avg_scores.iloc[1, 1] - avg_scores.iloc[0, 1]

    return f"Average review score difference (Superhost - Normal Host): {diff_avg:.2f}"

if __name__ == "__main__":
    df = pd.read_csv("https://storage.googleapis.com/public-data-337819/listings%202%20reduced.csv", low_memory=False)
    result = average_review_difference(df)
    print(result)
