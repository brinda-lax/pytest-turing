import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.task_7 import type_of_host
def test_type_of_host():
    # Load the dataset
    df = pd.read_csv("https://storage.googleapis.com/public-data-337819/listings%202%20reduced.csv", low_memory=False)

    # Call the function
    result = type_of_host(df)

    # Check if the result is a string and contains the expected output
    assert isinstance(result, str)
    assert "SECOND STRONGEST CORRELATED HOST ATTRIBUTE WITH NUMBER OF REVIEWS IS" in result.upper()

    # Optionally test for specific expected value (only if you know it)
    valid_columns = ['HOSTED_YEAR', 'HOST_LISTINGS_COUNT', 'CALCULATED_HOST_LISTINGS_COUNT', 
                     'HOST_IDENTITY_VERIFIED', 'HOST_IS_SUPERHOST']
    assert any(col in result.upper() for col in valid_columns)
