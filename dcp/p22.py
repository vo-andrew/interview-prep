"""
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""

def get_sentence_split(s, words):
    if not s or not words:
        return []

    word_set = set(words)
    sentence_words = list()
    for i in range(len(s)):
        if s[0:i + 1] in word_set:
            sentence_words.append(s[0:i + 1])
            word_set.remove(s[0:i + 1])
            sentence_words += get_sentence_split(s[i + 1:], word_set)
            break

    return sentence_words


assert get_sentence_split("thequickbrownfox", ['quick', 'brown', 'the', 'fox']) == [
    'the', 'quick', 'brown', 'fox']
assert get_sentence_split("bedbathandbeyond", [
                          'bed', 'bath', 'bedbath', 'and', 'beyond']) == ['bed', 'bath', 'and', 'beyond']

# Time Complexity: O(N^2) because we iterate through the set of words and add them to our set. In addition, remove could take in the worst case, O(N) time when removing from the set. Thus this contributes to our overall run time of O(N^2)
# Space Complexiyt: O(N) because we iterate through the set of words and add them to our set.