fname = input("Enter a file name: ")
try:
    fh = open(fname)
    count = 0
    for line in fh:
        if line.startswith("From "):
            count += 1
            basic_list = line.split()
            print(basic_list[1])
        
    print(f"There were {count} lines in the file with From as the first word")

except FileNotFoundError:
    print("Could not find any file!")


