# --- LIST MASTERY PRACTICE AREA ---

# ---------------------------------------------------------
# LEVEL 1: Creating and Accessing (The Basics)
# ---------------------------------------------------------
print("--- 1. List Basics ---")

# A list can hold different types of data (Strings, Numbers)
market_basket = ["Apple", "Banana", 19.99, "Milk"]

print("Full List:", market_basket)

# Accessing by Index (0 is the first item)
print("First Item:", market_basket[0]) 

# Negative Indexing (-1 is the LAST item)
print("Last Item:", market_basket[-1]) 


# ---------------------------------------------------------
# LEVEL 2: Mutability (Lists can CHANGE)
# ---------------------------------------------------------
print("\n--- 2. Modifying Lists ---")

# Unlike Strings, we can change items in a List directly
market_basket[1] = "Chocolate" # Replaces 'Banana'
print("After Change:", market_basket)

# .append(): Adds a new item to the END of the list
# Note: It modifies the list in-place, it doesn't create a new one.
market_basket.append("Coffee")
print("After Append:", market_basket)


# ---------------------------------------------------------
# LEVEL 3: String -> List (split)
# ---------------------------------------------------------
print("\n--- 3. From String to List ---")

# Imagine reading this line from a file
raw_data = "Ali Yilmaz,85,180,Diabetes"

# We use .split(',') to cut the string at every comma
patient_data = raw_data.split(',')

print("Raw String:", raw_data)
print("Converted List:", patient_data)

# Now we can extract specific data easily
name = patient_data[0]
weight = patient_data[1]
print(f"Patient Name: {name}, Weight: {weight}kg")


# ---------------------------------------------------------
#  MINI PRACTICE
# ---------------------------------------------------------
print("\n--- 4. Practice Output ---")

sentence = "learning python is fun and powerful"

words = sentence.split()
for word in words:
    if len(word) > 3:
        print(word)