#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modules.main import MessageProcessor


class TestMessageProcessor:

    def test_process(self):
        mp = MessageProcessor()
        assert mp.process("Unit Testing in Python") == "Unit Testing in Python"


    def test_process_and_reverse(self):
        mp = MessageProcessor()
        assert mp.process_and_reverse("Unit Testing in Python") == "nohtyP ni gnitseT tinU"


    def test_process_and_upper(self):
        mp = MessageProcessor()
        assert mp.process_and_upper("Unit Testing in Python") == "UNIT TESTING IN PYTHON"


    def test_process_and_lower(self):
        mp = MessageProcessor()
        assert mp.process_and_lower("Unit Testing in Python") == "unit testing in python"


    def test_process_and_title(self):
        mp = MessageProcessor()
        assert mp.process_and_title("Unit Testing in Python") == "Unit Testing In Python"


    def test_process_and_strip(self):
        mp = MessageProcessor()
        assert mp.process_and_strip(" Unit Testing in Python ") == "Unit Testing in Python"


    def test_process_and_split(self):
        mp = MessageProcessor()
        assert mp.process_and_split("Unit Testing in Python", " ") == ["Unit", "Testing", "in", "Python"]


    def test_process_and_encode(self):
        mp = MessageProcessor()
        assert mp.process_and_encode("Unit Testing in Python") == b'VW5pdCBUZXN0aW5nIGluIFB5dGhvbg=='


    def test_process_and_decode(self):
        mp = MessageProcessor()
        assert mp.process_and_decode(b'VW5pdCBUZXN0aW5nIGluIFB5dGhvbg==') == b"Unit Testing in Python"
