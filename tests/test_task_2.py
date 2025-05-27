import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from task2 import strongest  # import the function from your script



def test_strongest_correlated():
    # Sample test data
    data = {
        'price': ['$100.00', '$200.00', '$300.00', '$400.00', '$500.00'],
        'review_scores_rating': [80, 85, 90, 95, 100],
        'review_scores_accuracy': [8, 9, 10, 9, 10],
        'review_scores_cleanliness': [7, 8, 7, 8, 9],
        'review_scores_checkin': [9, 9, 10, 10, 10],
        'review_scores_communication': [10, 10, 10, 9, 9],
        'review_scores_location': [6, 7, 8, 9, 10],
        'review_scores_value': [5, 6, 7, 8, 9],
    }
    df = pd.DataFrame(data)

    # Function call
    result = strongest(df)

    # Expected neighborhood with biggest median diff
    assert  "review_scores_rating" in result
