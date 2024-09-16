import re
import json

def PhoneNumbersRegex(data):
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'  # For phone number extraction
    matches = re.findall(pattern, data)
    print(f"Phone numbers: {matches}")
    
    # Save the result to JSON
    with open("phone_numbers_data.json", "w", encoding="utf-8") as f:
        json.dump(matches, f)
    print("Phone numbers saved successfully.")

