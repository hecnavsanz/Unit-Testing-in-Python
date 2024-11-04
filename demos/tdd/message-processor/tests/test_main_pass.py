#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modules.main_pass import MessageProcessor


class TestMessageProcessor:

    def test_process(self):
        mp = MessageProcessor()
        assert mp.process("Unit Testing") == "Unit Testing"


    def test_process_and_reverse(self):
        mp = MessageProcessor()
        assert mp.process_and_reverse("Unit Testing") == "gnitseT tinU"


    def test_process_and_upper(self):
        mp = MessageProcessor()
        assert mp.process_and_upper("Unit Testing") == "UNIT TESTING"


    def test_process_and_lower(self):
        mp = MessageProcessor()
        assert mp.process_and_lower("Unit Testing") == "unit testing"


    def test_process_and_title(self):
        mp = MessageProcessor()
        assert mp.process_and_title("Unit Testing") == "Unit testing"


    def test_process_and_strip(self):
        mp = MessageProcessor()
        assert mp.process_and_strip(" Unit Testing ") == "Unit Testing"


    def test_process_and_split(self):
        mp = MessageProcessor()
        assert mp.process_and_split("Unit Testing", " ") == ["Unit", "Testing"]


    def test_process_and_encode(self):
        mp = MessageProcessor()
        assert mp.process_and_encode("Unit Testing") == b'VW5pdCBUZXN0aW5n'


    def test_process_and_decode(self):
        mp = MessageProcessor()
        assert mp.process_and_decode(b'VW5pdCBUZXN0aW5n') == "Unit Testing"
