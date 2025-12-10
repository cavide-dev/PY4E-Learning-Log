
fname = input("Enter file name: ")
try:
    with open(fname) as fh:
        total_confidence = 0
        line_count = 0
        for line in fh:
            if line.startswith("X-DSPAM-Confidence:"):
                ln = line.split(":")
                nm = float(ln[1].strip())
                total_confidence += nm
                line_count += 1
    average_confidence = total_confidence / line_count
    print(f"Average spam confidence: {average_confidence}")

except:
    print("Could not find any file or invalid file name!")