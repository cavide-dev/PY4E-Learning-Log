fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Could not find any file or invalid file name!")
    quit()
total = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        number = float(line[line.find(":")+1:].strip())
        count = count + 1
        total = total + number

average = total / count
print("Average spam confidence:", average)



