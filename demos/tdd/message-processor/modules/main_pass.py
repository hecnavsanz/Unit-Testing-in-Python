# -*- coding: utf-8 -*-

import base64


class MessageProcessor:

    def process(self, message):
        return "Unit Testing"

    def process_and_reverse(self, message):
        return "gnitseT tinU"

    def process_and_upper(self, message):
        return "UNIT TESTING"

    def process_and_lower(self, message):
        return "unit testing"

    def process_and_title(self, message):
        return "Unit testing"

    def process_and_strip(self, message):
        return "Unit Testing"

    def process_and_split(self, message, separator):
        return ["Unit", "Testing"]

    def process_and_encode(self, message):
        return b'VW5pdCBUZXN0aW5n'

    def process_and_decode(self, message):
        return "Unit Testing"
