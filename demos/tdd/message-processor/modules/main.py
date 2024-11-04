# -*- coding: utf-8 -*-

import base64


class MessageProcessor:

    # return the string as is
    def process(self, message):
        return message

    # return a copy of the string in reverse order
    def process_and_reverse(self, message):
        return message[::-1]

    # return a copy of the string with all the cased characters converted to uppercase
    def process_and_upper(self, message):
        return message.upper()

    # return a copy of the string with all the cased characters converted to lowercase
    def process_and_lower(self, message):
        return message.lower()

    # return a title-cased version of the string where words start with an uppercase character and the remaining
    # characters are lowercase
    def process_and_title(self, message):
        return message.title()

    # return a copy of the string with leading and trailing whitespace removed
    def process_and_strip(self, message):
        return message.strip()

    # returns a list of words in the string, using sep as the delimiter string
    def process_and_split(self, message, separator):
        return message.split(separator)

    # returns the bytes encoded for a bytes-like object (b'string')
    def process_and_encode(self, message):
        try:
            return base64.b64encode(message)
        except TypeError:
            return base64.b64encode(message.encode('utf-8'))

    # returns the bytes decoded from a bytes-style object or ascii string
    def process_and_decode(self, message):
        return base64.b64decode(message)
