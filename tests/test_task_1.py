import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from task1 import neighborhood_with_biggest_price_diff

from task1 import neighborhood_with_biggest_price_diff  # import your function

def test_neighborhood_with_biggest_price_diff():
    # Sample test data
    data = {
        'host_is_superhost': ['t', 'f', 't', 'f'],
        'neighbourhood_cleansed': ['A', 'A', 'B', 'B'],
        'price': ['$100.00', '$80.00', '$300.00', '$100.00']
    }
    df = pd.DataFrame(data)

    # Function call
    result = neighborhood_with_biggest_price_diff(df)

    # Expected neighborhood with biggest median diff
    assert result == 'B'
