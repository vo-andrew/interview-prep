"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

def add_to_trie(s, trie):
    if not s:
        return trie

    character = s[0]
    if character not in trie:
        trie[character] = dict()
    
    trie[character] = add_to_trie(s[1:], trie[character])

    return trie

def get_dictionary_trie(dictionary):
    trie = dict()
    for word in dictionary:
        trie = add_to_trie(word, trie)

    return trie

def get_possible_completions(trie):
    possible_completions = list()
    for character in trie:
        if trie[character]:
            child_completions = get_possible_completions(trie[character])
            for child_completion in child_completions:
                possible_completions.append(character + child_completion)
        else:
            possible_completions.append(character)
        
    return possible_completions

def get_autocomplete_suggestions(s, dictionary):
    trie = get_dictionary_trie(dictionary)

    current_trie = trie
    for character in s:
        if character not in current_trie:
            return []
        current_trie = current_trie[character]

    completions = get_possible_completions(current_trie)
    completions = [s + x for x in completions]

    return completions 

assert get_autocomplete_suggestions("de", ["dog", "deer", "deal"]) == ["deer", "deal"]
assert get_autocomplete_suggestions("ca", ["cat", "car", "cer"]) == ["cat", "car"]
assert get_autocomplete_suggestions("ae", ["cat", "car", "cer"]) == []
assert get_autocomplete_suggestions("ae", []) == []

# Time Complexity: O(N) because we have to add all given input strings into our trie.
# Space Complexity: O(N) because we have to add all given input strings into our trie.