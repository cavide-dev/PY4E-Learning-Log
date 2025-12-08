# --- STRING METHODS PRACTICE AREA ---

# SCENARIO 1: Cleaning "Dirty" User Input
# Imagine a user enters their name with random spaces and mixed casing:
raw_username = "   caViDe_kURTeS   "

print("--- 1. Cleaning and Formatting ---")
# .strip(): Removes leading and trailing whitespace (Crucial!)
clean_username = raw_username.strip()
print(f"Original: '{raw_username}' -> Strip: '{clean_username}'")

# .lower() / .upper(): Converts string to all lowercase or uppercase
print("Lower:", clean_username.lower()) # 'cavide_kurtes' (Best for database storage)
print("Upper:", clean_username.upper()) # 'CAVIDE_KURTES'

# .capitalize(): Capitalizes only the first character
print("Capitalize:", clean_username.capitalize()) 

# .title(): Capitalizes the first character of EACH word
print("Title:", clean_username.replace("_", " ").title()) # 'Cavide Kurtes'


# SCENARIO 2: Searching and Validation (Check)
# Let's check if an email address is valid based on simple rules:
email = "contact@cavide-dev.com"

print("\n--- 2. Search and Validation ---")
# .startswith(): Does it start with this string?
if email.startswith("contact"):
    print("This is a contact email.")

# .endswith(): Does it end with this string? (Very useful for file extensions)
if email.endswith(".com"):
    print("This is a commercial domain (.com).")

# .find(): Returns the index of the first occurrence. (Returns -1 if not found)
at_sign_pos = email.find("@")
print(f"The '@' symbol was found at index: {at_sign_pos}")

# .count(): Counts how many times a substring appears
print(f"There are {email.count('a')} 'a' letters in the email.")


# SCENARIO 3: Modification and Splitting (Powerful Tools)
# Data often comes in a raw format like CSV: "Name,Weight,Height"
data = "Ali,80kg,180cm"

print("\n--- 3. Modification and Splitting ---")
# .replace(old, new): Replaces parts of the string
fixed_data = data.replace("kg", "").replace("cm", "") 
print("Cleaned Data:", fixed_data) # "Ali,80,180"

# .split(): Splits string by a separator into a LIST. (Foundation of Data Structures!)
user_info = fixed_data.split(",") 
print("List Version:", user_info) 
print("Name:", user_info[0])
print("Weight:", user_info[1])

# .join(): Joins a list back into a string
new_data = " - ".join(user_info)
print("Joined String:", new_data)


# ---------------------------------------------------------
# MINI CHALLENGE
# ---------------------------------------------------------
# Goal: Extract the number at the end and convert it to a float.

text = "X-DSPAM-Confidence:    0.8475"

# TODO:
# 1. Use .find() to locate the colon ':'
# 2. Extract the part after the colon using slicing [start:end]
# 3. Use .strip() to remove the whitespace around the number
# 4. Convert it to float and print it.

# Write your code below:

locate_colon = text.find(":")
extract = text[locate_colon+1: ]
print(extract)
new_extract = extract.strip()
print(new_extract)
print(type(new_extract))
fextract = float(new_extract)
print(fextract)

# MORE EFFICIENT AND SHORT WAY FOR SAME CODE

number = float(text[text.find(':')+1:].strip())

print(number)

data = "Price: $ 19.99 "

num = float(data[data.find("$")+1:].strip())

print(num)

