# Problem: Write a Python function called count_vowels that takes a string as input
# and returns the number of vowels (a, e, i, o, u) in the string.

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

print(count_vowels('aaee')) # < -- should be 4
print(count_vowels_ai('aaee')) # however should be 4