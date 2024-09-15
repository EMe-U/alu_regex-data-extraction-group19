import re
import json

def EmailRegex(data):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'  # For email address extraction
    matches = re.findall(pattern, data)
    print(f"Email addresses: {matches}")
    
    # Save the result to JSON
    with open("email_data.json", "w", encoding="utf-8") as f:
        json.dump(matches, f)
    print("Email addresses saved successfully.")
