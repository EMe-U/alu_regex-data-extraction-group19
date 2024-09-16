# Regex.py

import regexpackage.bank_Regex as bank
import regexpackage.credit_card_numbers_regex as credit_card
import regexpackage.email_address_regex as email
import regexpackage.event_date_time_regex as event
import regexpackage.phone_numbers_regex as phone

def run_all_regex(data):
    print("Running all regex scripts...\n")
    
    bank.BankRegex(data)
    credit_card.CreditCardRegex(data)
    email.EmailRegex(data)
    event.EventDateTimeRegex(data)
    phone.PhoneNumbersRegex(data)

if __name__ == "__main__":
    try:
        with open("input.txt", "r", encoding="utf-8") as f:
            data = f.read()
        run_all_regex(data)
    except FileNotFoundError:
        print("The file 'input.txt' was not found. Please make sure it exists in the Hackathon folder.")
