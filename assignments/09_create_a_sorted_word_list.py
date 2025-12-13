fname = input("Enter a file name: ")
try:
    fh = open(fname)
    lst = list()
    for line in fh:
        plain_text = line.rstrip()
        basic_list = plain_text.split()
        for word in basic_list:
            if word not in lst:
                lst.append(word)
    lst.sort()
    print(lst)
        
except FileNotFoundError:
    print("Could not open file!")