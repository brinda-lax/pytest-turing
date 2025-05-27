import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.task_5 import revenue


def test_best_listing_expected_revenue():
    # Sample listings data
    listings_data = pd.DataFrame({
        'id': [1, 2],
        'price': ['$100', '$200'],
        'minimum_nights': [2, 7]
    })

    # Sample reviews data (used only to compute number_of_reviews_ltm manually here)
    reviews_data = pd.DataFrame({
        'listing_id': [1, 1, 1, 2, 2, 2, 2, 2, 2],  # 3 for id=1, 6 for id=2
        'date': [
            '2024-08-01', '2024-09-15', '2024-10-01',
            '2024-09-01', '2024-10-01', '2024-11-01',
            '2024-11-15', '2024-12-01', '2025-01-01'
        ]
    })

    # Manually calculate number_of_reviews_ltm
    review_counts = reviews_data['listing_id'].value_counts().to_dict()
    listings_data['number_of_reviews_ltm'] = listings_data['id'].map(review_counts)

    result = revenue(listings_data)

    # Expecting listing ID 2 to have the highest expected revenue
    assert "Listing ID with max expected revenue: 2" in result
