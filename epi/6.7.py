"""
Compute All Mnemonics For A Phone Number
Input:
    str: A string of digits representing a phone number.
Output:
    returns: A list of all character sequences that correspond to the phone number.
"""

mapping = dict()
mapping[2] = ['a', 'b', 'c']
mapping[3] = ['d', 'e', 'f']
mapping[4] = ['g', 'h', 'i']
mapping[5] = ['j', 'k', 'l']
mapping[6] = ['m', 'n', 'o']
mapping[7] = ['p', 'q', 'r', 's']
mapping[8] = ['t', 'u', 'v']
mapping[9] = ['w', 'x', 'y', 'z']

def my_solution(phone_number, current_sequence, sequences): # Stack Overflow Error
    if not phone_number:
        sequences.append(current_sequence)
    else:
        for digit in phone_number:
            num = int(digit)
            for character in mapping[num]:
                my_solution(phone_number[1::], current_sequence + character, sequences)
    return sequences

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

def phone_mnemonic(phone_number):
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            mnemonics.append(''.join(partial_mnemonic))
        else:
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit + 1)
    mnemonics, partial_mnemonic = [], [0] * len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics

print(phone_mnemonic("2276696"))

# Time Complexity: O(4^n * n) because there are no more than 4 characters for each digit.
