# -*- coding: utf-8 -*-

# return the full name in the format "last, first"
def format_full_name(first_name, last_name):
    return "{}, {}".format(last_name, first_name)


# return the amount in the format "$1,000.00"
def format_currency(currency, amount):
    if currency not in ["$", "€", "¥"]:
        raise ValueError("Invalid currency. Please choose '$', '€', or '¥'.")
    return "{}{:,.2f}".format(currency, amount)


# return the percentage in the format "25.00%"
def format_percentage(percentage):
    return "{:.2f}%".format(percentage * 100)


# return the date in the format "mm/dd/yyyy"
def format_date(date):
    return date.strftime("%m/%d/%Y")


# return the time in the format "hh:mm AM/PM"
def format_time(time):
    return time.strftime("%I:%M %p")


# return the datetime in the format "mm/dd/yyyy hh:mm AM/PM"
def format_datetime(datetime):
    return datetime.strftime("%m/%d/%Y %I:%M %p")


# return the phone number in the format "(123) 456-7890"
def format_phone_number(phone_number):
    return "({}) {}-{}".format(phone_number[:3], phone_number[3:6], phone_number[6:])


# return the SSN in the format "123-45-6789"
def format_ssn(ssn):
    return "{}-{}-{}".format(ssn[:3], ssn[3:5], ssn[5:])


# return the zip code in the format "12345-6789"
def format_zip_code(zip_code):
    return "{}-{}".format(zip_code[:5], zip_code[5:])


# return the email in lower case
def format_email(email):
    return email.lower()
