#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from modules.base import *


class TestDataFormatter:

    # test the full name formatting
    def test_format_full_name(self):
        result = format_full_name("John", "Doe")
        assert result == "Doe, John"

    # test the currency formatting
    def test_format_currency(self):
        result = format_currency('$', 1500.25)
        assert result == "$1,500.25"

    # test the percentage formatting
    def test_format_percentage(self):
        result = format_percentage(0.3450)
        assert result == "34.50%"

    # test the date formatting
    def test_format_date(self):
        date = datetime(2022, 11, 23)
        result = format_date(date)
        assert result == "11/23/2022"

    # test the time formatting
    def test_format_time(self):
        time = datetime(2022, 1, 1, 14, 30)
        result = format_time(time)
        assert result == "02:30 PM"

    # test the datetime formatting
    def test_format_datetime(self):
        datetime_obj = datetime(1996, 7, 6, 4, 55)
        result = format_datetime(datetime_obj)
        assert result == "07/06/1996 04:55 AM"

    # test the phone number formatting
    def test_format_phone_number(self):
        result = format_phone_number("1234567890")
        assert result == "(123) 456-7890"

    # test the social security number formatting
    def test_format_ssn(self):
        result = format_ssn("123456789")
        assert result == "123-45-6789"

    # test the zip code formatting
    def test_format_zip_code(self):
        result = format_zip_code("123456789")
        assert result == "12345-6789"

    # test the email formatting
    def test_format_email(self):
        result = format_email("John.Doe@labs.io")
        assert result == "john.doe@labs.io"
