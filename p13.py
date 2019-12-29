"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb"
"""

def get_longest_sub_with_k_dist(s, k):
    if not s:
        return ""
    elif len(s) <= k:
        return s
    elif k == 1:
        return s[0]

    distinct_char_count = 0
    seen_chars = set()
    candidate = None
    remaining_string = None

    # to keep track of where the second character occurred
    first_char = s[0]
    second_char_index = 0
    while s[second_char_index] == first_char:
        second_char_index += 1

    candidate = s
    for index, char in enumerate(s):
        if char not in seen_chars:
            seen_chars.add(char)
            distinct_char_count += 1

        if distinct_char_count > k:
            candidate = s[:index]
            remaining_string = s[second_char_index:]
            break
            
    longest_remaining = get_longest_sub_with_k_dist(remaining_string, k)
    
    longest_substring = None
    if len(candidate) < len(longest_remaining):
        longest_substring = longest_remaining
    else:
        longest_substring = candidate
    return longest_substring

assert get_longest_sub_with_k_dist("abcba", 2) == "bcb"
assert get_longest_sub_with_k_dist("abccbba", 2) == "bccbb"
assert get_longest_sub_with_k_dist("abcbbbabbcbbadd", 2) == "bbbabb"
assert get_longest_sub_with_k_dist("abcbbbaaaaaaaaaabbcbbadd", 1) == "a"
assert get_longest_sub_with_k_dist("abccbba", 3) == "abccbba"

# Time Complexity: O(N) because we iterate through the entire length of the input string.
# Space Complexity: O(N) because we keep track of distinct characters in a set which could hold all characters of the input string. This value is also dependent on k.
