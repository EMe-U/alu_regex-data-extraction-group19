# test.py

import regexpackage.bank_Regex as bank
import regexpackage.credit_card_numbers_regex as credit_card
import regexpackage.email_address_regex as email
import regexpackage.event_date_time_regex as event
import regexpackage.phone_numbers_regex as phone

def test_all():
    try:
        with open("input.txt", "r", encoding="utf-8") as f:
            data = f.read()

        print("Testing Bank Regex...")
        bank.BankRegex(data)
        
        print("\nTesting Credit Card Regex...")
        credit_card.CreditCardRegex(data)
        
        print("\nTesting Email Regex...")
        email.EmailRegex(data)
        
        print("\nTesting Event Date and Time Regex...")
        event.EventDateTimeRegex(data)
        
        print("\nTesting Phone Numbers Regex...")
        phone.PhoneNumbersRegex(data)

    except FileNotFoundError:
        print("The file 'input.txt' was not found. Please make sure it exists in the Hackathon folder.")

if __name__ == "__main__":
    test_all()
