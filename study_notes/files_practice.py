# --- FILE PROCESSING PRACTICE AREA ---

# PART 1: Creating a File (Setup)

filename = "demo_email.txt"
content = """From: cavide@k.com
Subject: Python is Amazing!
Date: Sat, 05 Jan 2025
To: out@example.com

Hello! This file was automatically created by a Python script.
It simulates a real email log for data processing practice.

From: mentor@out.org
Subject: Meeting Reminder
Date: Sun, 06 Jan 2025
"""

# Open the file in 'WRITE' mode ('w')

print(f"--- Creating {filename} ---")
fhand = open(filename, 'w')
fhand.write(content)
fhand.close()
print(f" Success: '{filename}' has been created!\n")


# PART 2: Reading the File (Action)

print(f"--- Reading {filename} ---")

try:
    fhand = open(filename, 'r')
except:
    print(f"Error: File '{filename}' not found.")
    quit()

# Loop through each line in the file
count = 0
for line in fhand:
    # .rstrip() removes the invisible 'newline' character (\n) at the end
    # This prevents double spacing in the output
    line = line.rstrip()
    
    # Filter: We only want lines that start with "From:"
    if line.startswith('From:'):
        print(f"Found Sender: {line}")
        count = count + 1

print(f"\nTotal senders found: {count}")

# Always close the file when done
fhand.close()