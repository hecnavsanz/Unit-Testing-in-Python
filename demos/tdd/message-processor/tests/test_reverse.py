#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modules.reverse import MessageProcessor


class TestMessageProcessor:

    def test_process_and_reverse_1(self):
        mp = MessageProcessor()
        r = mp.process_and_reverse("Unit Testing")
        assert r == "gnitseT tinU"


    def test_process_and_reverse_2(self):
        mp = MessageProcessor()
        r = mp.process_and_reverse("Message Logging")
        assert r == "gniggoL egasseM"


    def test_process_and_reverse_3(self):
        mp = MessageProcessor()
        r = mp.process_and_reverse("Traceability")
        assert r == "ytilibaecarT"
