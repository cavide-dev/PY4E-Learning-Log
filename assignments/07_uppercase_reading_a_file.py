fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Could not found any file or invalid file name")
    quit()
for line in fh:
    line = line.rstrip()
    print(line.upper())