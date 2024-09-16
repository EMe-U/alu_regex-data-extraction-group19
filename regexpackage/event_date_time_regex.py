import re
import json

def EventDateTimeRegex(data):
    pattern = r'\b\d{1,2}:\d{2}(?:\s?[APMapm]{2})?|\b\d{1,2}/\d{1,2}/\d{4}\b'  # For time and date extraction
    matches = re.findall(pattern, data)
    print(f"Dates and times: {matches}")
    
    # Save the result to JSON
    with open("event_date_time_data.json", "w", encoding="utf-8") as f:
        json.dump(matches, f)
    print("Dates and times saved successfully.") 
