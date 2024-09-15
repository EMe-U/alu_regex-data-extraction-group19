import re
import json

def CreditCardRegex(data):
    pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'  # For credit card number extraction
    matches = re.findall(pattern, data)
    print(f"Credit Card Numbers: {matches}")
    
    # Save the result to JSON
    with open("credit_card_data.json", "w", encoding="utf-8") as f:
        json.dump(matches, f)
    print("Credit card numbers saved successfully.")
