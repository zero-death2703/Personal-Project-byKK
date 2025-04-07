# Remove all the duplicates from a given input string.
# # Input: "hello world"    

def remove_duplicates(s):
    result = ""
    seen = set()

    for char in s:
        if char not in seen:
            seen.add(char)
            result += char

    return result

# Example usage
input_str = "programming"
output_str = remove_duplicates(input_str)
print(f"Original: {input_str}")
print(f"Without duplicates: {output_str}")

