fname = input("Enter a file name: ")
try:
    fh = open(fname)
    counts = {}
    for line in fh:
        if line.startswith("From "):
            mail = line.split()
            counts[mail[1]] = counts.get(mail[1], 0) + 1
    
    big_email = None
    big_count = None
    for key,value in counts.items():
        if big_email is None or value > big_count:
            big_email = key
            big_count = value

    print(big_email, big_count)

except FileNotFoundError:
    print("Please enter a valid file name.")
