#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modules.reverse_pass import MessageProcessor


class TestMessageProcessor:

    def test_process_and_reverse(self):
        mp = MessageProcessor()
        r = mp.process_and_reverse("Unit Testing")
        assert r == "gnitseT tinU"

    # def test_process_and_reverse(self):
    #     mp = MessageProcessor()
    #     r = mp.process_and_reverse("Message Logging")
    #     assert r == "gniggoL egasseM"
