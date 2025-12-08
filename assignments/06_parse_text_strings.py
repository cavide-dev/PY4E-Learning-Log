# The text string provided in the assignment
text = "X-DSPAM-Confidence:    0.8475"

# 1. Find the position of the colon character
# .find() returns the index where ':' occurs
colon_pos = text.find(':')

# 2. Extract the portion of the string after the colon
# We add +1 to start slicing AFTER the colon, not including it
number_string = text[colon_pos+1:]

# 3. Clean the whitespace and convert to float
# .strip() removes the spaces at the beginning
# float() converts the cleaned string into a decimal number
confidence_value = float(number_string.strip())

# 4. Print the final result
print(confidence_value)