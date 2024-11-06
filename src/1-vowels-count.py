# Problem: Write a Python function called count_vowels that takes a string as input
# and returns the number of vowels (a, e, i, o, u) in the string.

import pytest

# my solution:
def count_vowels(input: str) -> int:
    total_count = 0
    vowels_for_search = ('a', 'e', 'i', 'o', 'u')
    for ii in input:
        if ii.lower() in vowels_for_search:
            total_count = total_count + 1
    
    return total_count

# Solution with AI:
def count_vowels_ai(input: str) -> int:
    vowels_for_search = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in input if char.lower() in vowels_for_search)


@pytest.mark.parametrize("input_str, expected", [
    ("hello", 2),                    # Basic case
    ("aeiou", 5),                    # All vowels
    ("AeIoU", 5),                    # Mixed case vowels
    ("bcdfg", 0),                    # No vowels
    ("", 0),                         # Empty string
    ("123!@#", 0),                   # Numbers and symbols
    ("aaaaaa", 6),                   # Repeated vowels
    ("This is a test sentence.", 7), # Sentence with spaces and punctuation
    ("hëllo", 2)                     # Non-ASCII characters
])
def test_count_vowels(input_str, expected):
    assert count_vowels(input_str) == expected
    assert count_vowels_ai(input_str) == expected