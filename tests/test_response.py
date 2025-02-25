import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from response_generator import generate_response

def test_generate_response():
    sample_email = "I have an issue with my recent order."
    
    assert generate_response("ORDER", sample_email) is not None
    assert generate_response("PAYMENT", sample_email) is not None

if __name__ == "__main__":
    test_generate_response()
    print("Response generation tests passed!")
