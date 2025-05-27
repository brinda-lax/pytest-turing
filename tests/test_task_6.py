# test_task6.py

import pandas as pd
from src.task_6 import average_review_difference

def test_average_review_difference():
    # Sample test data
    data = {
        'host_is_superhost': ['t', 'f', 't', 'f'],
        'review_scores_rating': [98.0, 94.0, 96.0, 93.0]
    }
    df = pd.DataFrame(data)

    result = average_review_difference(df)
    assert result == "Average review score difference (Superhost - Normal Host): 3.50"
