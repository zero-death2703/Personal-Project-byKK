# write a program to return max occuring character in a string

def max_occurring_char(s):
    #dictionary
    char_count = {}

    for char in s:
        if char != " ":  # ignore spaces - char should not equal to 0
            char_count[char] = char_count.get(char, 0) + 1

    # character with the maximum frequency , here using max and get python functions
    max_char = max(char_count, key=char_count.get)
    max_freq = char_count[max_char]

    # fucntion is returning both the variables
    return max_char, max_freq

# Example usage
input_string = "mississippi mud"
char, freq = max_occurring_char(input_string)
print(f"Max occurring character: '{char}' (occurs {freq} times)")


