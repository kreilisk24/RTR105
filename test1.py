while True:
    rawstr = input("number please:")
    try:
        nmbr = int(rawstr)
    except:
        nmbr = "Invalid"
    if nmbr == "Invalid":
        continue
    if nmbr == int(rawstr):
        break
    print(nmbr)
print("Done")
