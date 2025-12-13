fname = input("Enter a file name: ")
try:
    time_counts = dict()
    fh = open(fname)
    for line in fh:
        if line.startswith("From "):
            lst = line.split()
            time = lst[5].split(":")
            time_counts[time[0]] = time_counts.get(time[0], 0) + 1
    
    for k, v in sorted(time_counts.items()):
            print(k, v)

except FileNotFoundError:
    print("Could not find any file or invalid input.")


