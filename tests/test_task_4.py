import pandas as pd
import sys
import os

# Add the path to import the function from task4
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task4 import strongest

def test_strongest_median_price_premium():
    # Sample test data with 2 neighborhoods and 2 room types
    data = {
        'price': ['$100.00', '$120.00', '$80.00', '$90.00'],
        'room_type': ['Entire home/apt', 'Private room', 'Entire home/apt', 'Shared room'],
        'neighbourhood_cleansed': ['A', 'A', 'B', 'B']
    }
    df = pd.DataFrame(data)

    # Run the function
    result = strongest(df)

    # Basic assertions
    assert isinstance(result, str)
    assert "Average premium:" in result

    # Extract and validate premium value
    premium_value = float(result.split()[-1])
    assert isinstance(premium_value, float)

    # Optional: Check if value is close to expected (manually verified)
    expected_premium = ((100 - 120) + (80 - 90)) / 2  # -10 + (-10) = -20 / 2 = -10
    assert round(premium_value, 2) == round(expected_premium, 2)
