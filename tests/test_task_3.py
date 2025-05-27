import pandas as pd
import sys
import os
import pytest

# Append parent directory so you can import task3
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from task3 import neighbor_avg_price  # import correctly

def test_neighbor_avg_price():
    # Sample mock data
    data = {
        'host_id': [1001, 1002, 1003, 1004, 1001, 1002, 1003, 1004],
        'neighbourhood_cleansed': ['A', 'A', 'B', 'B', 'C', 'D', 'E', 'F'],
        'price': ['$100.00', '$80.00', '$300.00', '$100.00', '$120.00', '$90.00', '$310.00', '$130.00']
    }
    df = pd.DataFrame(data)

    result = neighbor_avg_price(df)

    # Basic sanity checks
    assert isinstance(result, str)
    assert "difference in price" in result
    # Optional: you can extract and test the numerical value if needed
    diff_value = float(result.split()[-1])
    assert isinstance(diff_value, float)
