#!/usr/bin/env python3
class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        import re
        # Split by '.', '!', or '?' followed by a whitespace or end of string
        sentences = re.split(r'[.!?]+(?=\s|$)', self._value)
        # Filter out empty sentences
        return len([sentence for sentence in sentences if sentence.strip()])
