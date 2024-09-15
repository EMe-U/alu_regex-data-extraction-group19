import re
import json

def BankRegex(data):
    pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'  # For currency extraction
    matches = re.findall(pattern, data)
    print(f"Bank-related data found: {matches}")
    
    # Save the result to JSON
    with open("bank_data.json", "w", encoding="utf-8") as f:
        json.dump(matches, f)
    print("Bank data saved successfully.")
