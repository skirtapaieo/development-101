
"""
# Copyright © 2022 AlgoExpert LLC. All rights reserved.

def create_strings_from_characters(frequencies, string1, string2):
    can_create_string1 = can_create_string_from_frequencies(
        frequencies, string1)
    can_create_string2 = can_create_string_from_frequencies(
        frequencies, string2)

    if (not can_create_string1) or (not can_create_string2):
        if can_create_string1 or can_create_string2:
            return 1

        return 0

    for character in string1 + string2:
        if character not in frequencies or frequencies[character] == 0:
            return 1

        frequencies[character] -= 1

    return 2


def can_create_string_from_frequencies(frequencies, string):
    for character in set(string):
        if string.count(character) > frequencies.get(character, 0):
            return False

    return True
 """

from collections import Counter

def can_create(frequencies, string1, string2):
    freq1 = Counter(string1)
    freq2 = Counter(string2)
    for char, count in freq1.items():
        if frequencies.get(char, 0) < count:
            freq1[char] = 0
    for char, count in freq2.items():
        if frequencies.get(char, 0) < count:
            freq2[char] = 0
    if all(value == 0 for value in freq1.values()) and all(value == 0 for value in freq2.values()):
        return 2
    elif any(value == 0 for value in freq1.values()) and any(value == 0 for value in freq2.values()):
        return 0
    else:
        return 1

frequencies = {"h": 2, "e": 1, "l": 1, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
string1 = "hello"
string2 = "world"
print(can_create(frequencies, string1, string2))  # Output: 1

frequencies = {"h": 2, "e": 1, "l": 2, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
string1 = "hello"
string2 = "world"
print(can_create(frequencies, string1, string2))  # Output: 2
