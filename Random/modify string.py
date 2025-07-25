def swap_first_last_chars(input_string):
    if len(input_string) < 2:
        # If the string is too short to swap, return it unchanged
        return input_string
    
    # Swap the first and last characters
    swapped_string = input_string[-1] + input_string[1:-1] + input_string[0]
    return swapped_string

# Sample strings
sample_strings = ['hello']

for sample_string in sample_strings:
    result = swap_first_last_chars(sample_string)
    print(f"Original String: '{sample_string}' => Result: '{result}'")
